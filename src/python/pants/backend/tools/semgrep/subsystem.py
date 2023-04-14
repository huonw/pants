# Copyright 2022 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from pants.backend.python.goals import lockfile
from pants.backend.python.goals.export import ExportPythonTool, ExportPythonToolSentinel
from pants.backend.python.goals.lockfile import GeneratePythonLockfile
from pants.backend.python.subsystems.python_tool_base import ExportToolOption, PythonToolBase
from pants.backend.python.target_types import ConsoleScript
from pants.backend.python.util_rules.pex_requirements import GeneratePythonToolLockfileSentinel
from pants.core.goals.generate_lockfiles import GenerateToolLockfileSentinel
from pants.engine.rules import Rule, collect_rules, rule
from pants.engine.target import Dependencies, FieldSet, SingleSourceField, Target
from pants.engine.unions import UnionRule
from pants.option.option_types import ArgsListOption, BoolOption, SkipOption, StrListOption
from pants.util.docutil import git_url


@dataclass(frozen=True)
class SemgrepFieldSet(FieldSet):
    required_fields = (SingleSourceField, Dependencies)
    source: SingleSourceField
    dependencies: Dependencies

    @classmethod
    def opt_out(cls, tgt: Target) -> bool:
        # FIXME: global skip_semgrep field?
        return False


class Semgrep(PythonToolBase):
    name = "Semgrep"
    options_scope = "semgrep"
    help = "Lightweight static analysis for many languages. Find bug variants with patterns that look like source code. (https://semgrep.dev/)"

    default_version = "semgrep==1.14.0"
    default_main = ConsoleScript("semgrep")

    register_interpreter_constraints = True
    default_interpreter_constraints = ["CPython>=3.7,<4"]

    register_lockfile = True
    default_lockfile_resource = ("pants.backend.tools.semgrep", "semgrep.lock")
    default_lockfile_path = "src/python/pants/backend/tools/semgrep/semgrep.lock"
    default_lockfile_url = git_url(default_lockfile_path)

    export = ExportToolOption()

    args = ArgsListOption(example="--verbose")

    skip = SkipOption("lint")

    tailor_rule_targets = BoolOption(
        default=True,
        help="If true, add `semgrep_rule_sources` targets with the `tailor` goal.",
        advanced=True,
    )

    acknowledge_nested_semgrepignore_files_are_not_used = BoolOption(
        default=False,
        help="Set to true suppress the warning about `.semgrepignore` files not at the build root not being used",
    )

    force = BoolOption(
        default=False,
        help="If true, semgrep is always run, even if the input files haven't changed. This can be used to run cloud rulesets like `--semgrep-force --semgrep-args='--config p/python`.",
        advanced=True,
    )


class SemgrepLockfileSentinel(GeneratePythonToolLockfileSentinel):
    resolve_name = Semgrep.options_scope


@rule
def setup_semgrep_lockfile(_: SemgrepLockfileSentinel, semgrep: Semgrep) -> GeneratePythonLockfile:
    return semgrep.to_lockfile_request()


class SemgrepExportSentinel(ExportPythonToolSentinel):
    pass


@rule
def semgrep_export(_: SemgrepExportSentinel, semgrep: Semgrep) -> ExportPythonTool:
    if not semgrep.export:
        return ExportPythonTool(resolve_name=semgrep.options_scope, pex_request=None)
    return ExportPythonTool(
        resolve_name=semgrep.options_scope, pex_request=semgrep.to_pex_request()
    )


def rules() -> Iterable[Rule | UnionRule]:
    return (
        *collect_rules(),
        *lockfile.rules(),
        UnionRule(GenerateToolLockfileSentinel, SemgrepLockfileSentinel),
        UnionRule(ExportPythonToolSentinel, SemgrepExportSentinel),
    )