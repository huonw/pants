# Copyright 2021 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

import collections
import hashlib
import json
from dataclasses import asdict, dataclass, field, is_dataclass, replace

# FIXME: only 3.9+
from graphlib import TopologicalSorter
from json import encoder
from typing import Any, Iterable, Mapping

from typing_extensions import Protocol, runtime_checkable

from pants.engine.collection import Collection
from pants.engine.console import Console
from pants.engine.fs import Snapshot
from pants.engine.goal import Goal, GoalSubsystem, Outputting
from pants.engine.rules import Get, MultiGet, collect_rules, goal_rule, rule
from pants.engine.target import (
    Dependencies,
    DependenciesRequest,
    Field,
    HydratedSources,
    HydrateSourcesRequest,
    SourcesField,
    Target,
    Targets,
    TransitiveTargets,
    TransitiveTargetsRequest,
    UnexpandedTargets,
)
from pants.option.option_types import BoolOption


@runtime_checkable
class Dictable(Protocol):
    """Make possible to avoid adding concrete types to serialize objects."""

    def asdict(self) -> Mapping[str, Any]:
        ...


class PeekSubsystem(Outputting, GoalSubsystem):
    """Display detailed target information in JSON form."""

    name = "peek"
    help = "Display BUILD target info"

    exclude_defaults = BoolOption(
        default=False,
        help="Whether to leave off values that match the target-defined default values.",
    )

    include_transitive_fingerprints = BoolOption(
        default=False,
        help="Whether to include a `transitive_fingerprint` key.",
    )


class Peek(Goal):
    subsystem_cls = PeekSubsystem
    environment_behavior = Goal.EnvironmentBehavior.LOCAL_ONLY


def _normalize_value(val: Any) -> Any:
    if isinstance(val, collections.abc.Mapping):
        return {str(k): _normalize_value(v) for k, v in val.items()}
    return val


@dataclass(frozen=True)
class TargetData:
    target: Target
    # Sources may not be registered on the target, so we'll have nothing to expand.
    expanded_sources: Snapshot | None
    expanded_dependencies: tuple[str, ...]

    intransitive_fingerprint: str = field(default="", init=False)
    transitive_fingerprint: str | None = None

    def __post_init__(self) -> None:
        d = self.to_dict(
            exclude_defaults=False, include_intransitive_and_transitive_fingerprints=False
        )
        s = json.dumps(d, cls=_PeekJsonEncoder)
        super().__setattr__("intransitive_fingerprint", hashlib.sha256(s.encode()).hexdigest())

    def to_dict(
        self,
        exclude_defaults: bool = False,
        include_intransitive_and_transitive_fingerprints: bool = True,
    ) -> dict:
        nothing = object()
        fields = {
            (
                f"{k.alias}_raw" if issubclass(k, (SourcesField, Dependencies)) else k.alias
            ): _normalize_value(v.value)
            for k, v in self.target.field_values.items()
            if not (exclude_defaults and getattr(k, "default", nothing) == v.value)
        }

        fields["dependencies"] = self.expanded_dependencies
        if self.expanded_sources is not None:
            fields["sources"] = self.expanded_sources.files
            fields["sources_fingerprint"] = self.expanded_sources.digest.fingerprint

        if include_intransitive_and_transitive_fingerprints:
            fields["intransitive_fingerprint"] = self.intransitive_fingerprint

            if self.transitive_fingerprint is not None:
                fields["transitive_fingerprint"] = self.transitive_fingerprint

        return {
            "address": self.target.address.spec,
            "target_type": self.target.alias,
            **dict(sorted(fields.items())),
        }


class TargetDatas(Collection[TargetData]):
    pass


def render_json(tds: Iterable[TargetData], exclude_defaults: bool = False) -> str:
    return f"{json.dumps([td.to_dict(exclude_defaults) for td in tds], indent=2, cls=_PeekJsonEncoder)}\n"


class _PeekJsonEncoder(json.JSONEncoder):
    """Allow us to serialize some commmonly found types in BUILD files."""

    def default(self, o):
        """Return a serializable object for o."""
        if isinstance(o, str):  # early exit prevents strings from being treated as sequences
            return o
        if o is None:
            return o
        if is_dataclass(o):
            return asdict(o)
        if isinstance(o, collections.abc.Mapping):
            return dict(o)
        if (
            isinstance(o, collections.abc.Sequence)
            or isinstance(o, set)
            or isinstance(o, collections.abc.Set)
        ):
            return list(o)
        if isinstance(o, Field):
            return self.default(o.value)
        if isinstance(o, Dictable):
            return o.asdict()
        try:
            return super().default(o)
        except TypeError:
            return str(o)


@rule
async def get_target_data(
    # NB: We must preserve target generators, not replace with their generated targets.
    targets: UnexpandedTargets,
    subsys: PeekSubsystem,
) -> TargetDatas:
    sorted_targets = sorted(targets, key=lambda tgt: tgt.address)

    if subsys.include_transitive_fingerprints:
        transitive_targets = await Get(
            TransitiveTargets,
            TransitiveTargetsRequest(roots=tuple(tgt.address for tgt in sorted_targets)),
        )
        targets_to_analyze = transitive_targets.closure
    else:
        targets_to_analyze = sorted_targets

    # We "hydrate" sources fields with the engine, but not every target has them registered.
    targets_with_sources = [tgt for tgt in targets_to_analyze if tgt.has_field(SourcesField)]

    # NB: When determining dependencies, we replace target generators with their generated targets.
    dependencies_per_target = await MultiGet(
        Get(
            Targets,
            DependenciesRequest(tgt.get(Dependencies), include_special_cased_deps=True),
        )
        for tgt in targets_to_analyze
    )
    hydrated_sources_per_target = await MultiGet(
        Get(HydratedSources, HydrateSourcesRequest(tgt[SourcesField]))
        for tgt in targets_with_sources
    )

    expanded_dependencies = {
        tgt.address: tuple(dep.address for dep in deps)
        for tgt, deps in zip(targets_to_analyze, dependencies_per_target)
    }
    expanded_sources_map = {
        tgt.address: hs.snapshot
        for tgt, hs in zip(targets_with_sources, hydrated_sources_per_target)
    }

    data = {
        tgt.address.spec: TargetData(
            tgt,
            expanded_dependencies=tuple(a.spec for a in expanded_dependencies.get(tgt.address, ())),
            expanded_sources=expanded_sources_map.get(tgt.address),
        )
        for tgt in targets_to_analyze
    }

    if subsys.include_transitive_fingerprints:
        sorter = TopologicalSorter()
        for address, deps in expanded_dependencies.items():
            sorter.add(address, *deps)

        for address in sorter.static_order():
            deps = [
                (dep, data[dep].transitive_fingerprint)
                for dep in sorted(data[address.spec].expanded_dependencies)
            ]
            this = data[address.spec]
            serialized = json.dumps([this.intransitive_fingerprint, deps])
            data[address.spec] = replace(
                this, transitive_fingerprint=hashlib.sha256(serialized.encode()).hexdigest()
            )

    # TODO: cycles occur in practice; can be handled by instead processing strongly connected
    # components

    return TargetDatas(data[tgt.address.spec] for tgt in sorted_targets)


@goal_rule
async def peek(
    console: Console,
    subsys: PeekSubsystem,
    targets: UnexpandedTargets,
) -> Peek:
    tds = await Get(TargetDatas, UnexpandedTargets, targets)
    output = render_json(tds, subsys.exclude_defaults)
    with subsys.output(console) as write_stdout:
        write_stdout(output)
    return Peek(exit_code=0)


def rules():
    return collect_rules()
