# Copyright 2023 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).
from __future__ import annotations

import logging
import shlex
import subprocess

logger = logging.getLogger(__name__)

MAIN_REPO_SLUG = "pantsbuild/pants"
MAIN_REPO = f"https://github.com/{MAIN_REPO_SLUG}"


def _run(
    exe: str,
    args: tuple[None | str, ...],
    check: bool,
    capture_stdout: bool,
) -> str:
    cmd = [exe, *(a for a in args if a is not None)]
    logger.info("running: %s", shlex.join(cmd))
    result = subprocess.run(
        cmd,
        check=check,
        stdout=subprocess.PIPE if capture_stdout else None,
        text=True,
    )
    stdout = "" if result.stdout is None else result.stdout.strip()
    logger.debug("returncode: %s, stdout: %s", result.returncode, stdout)
    return stdout


def git(*args: None | str, check: bool = True, capture_stdout: bool = True) -> str:
    """Run `git *args`, skipping any Nones."""
    return _run("git", args, check=check, capture_stdout=capture_stdout)


def git_rev_parse(rev: str, *, verify: bool = True, abbrev_ref: bool = False) -> str:
    return git(
        "rev-parse", "--verify" if verify else None, "--abbrev-ref" if abbrev_ref else None, rev
    )


def git_fetch(rev: str) -> str:
    """Fetch rev (e.g. branch or a SHA) from the upstream repository and return its SHA."""
    git("fetch", MAIN_REPO, rev)
    return git_rev_parse("FETCH_HEAD")
