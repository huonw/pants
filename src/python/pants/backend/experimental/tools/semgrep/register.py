# Copyright 2022 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

"""Lightweight static analysis for many languages. Find bug variants with patterns that look like
source code.

See https://semgrep.dev/ for details.
"""

from __future__ import annotations

from typing import Iterable

from pants.backend.python.goals import lockfile as python_lockfile
from pants.backend.tools.semgrep import dependency_inference
from pants.backend.tools.semgrep import rules as semgrep_rules
from pants.backend.tools.semgrep import subsystem as subsystem
from pants.backend.tools.semgrep import tailor
from pants.backend.tools.semgrep.target_types import (
    SemgrepRuleSource,
    SemgrepRuleSourcesGeneratorTarget,
)
from pants.engine.rules import Rule
from pants.engine.unions import UnionRule


def target_types():
    return [SemgrepRuleSource, SemgrepRuleSourcesGeneratorTarget]


def rules() -> Iterable[Rule | UnionRule]:
    return (
        *semgrep_rules.rules(),
        *subsystem.rules(),
        *python_lockfile.rules(),
        *dependency_inference.rules(),
        *tailor.rules(),
    )