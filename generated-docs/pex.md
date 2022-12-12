
How Pants uses Pex to run Python subprocesses.

Backend: <span style="color: purple"><code>pants.backend.awslambda.python, pants.backend.codegen.protobuf.python, pants.backend.docker, pants.backend.docker.lint.hadolint, pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.helm, pants.backend.experimental.python, pants.backend.experimental.python.lint.add_trailing_comma, pants.backend.experimental.python.lint.autoflake, pants.backend.experimental.python.lint.pyupgrade, pants.backend.experimental.terraform, pants.backend.google_cloud_function.python, pants.backend.python, pants.backend.python.lint.bandit, pants.backend.python.lint.black, pants.backend.python.lint.docformatter, pants.backend.python.lint.flake8, pants.backend.python.lint.isort, pants.backend.python.lint.pylint, pants.backend.python.lint.yapf, pants.backend.python.typecheck.mypy, pants.core</code></span>
Config section: <span style="color: purple"><code>[pex]</code></span>

## Basic options

None

## Advanced options

<div style="color: purple">

### `verbosity`

  <code>--pex-verbosity=&lt;int&gt;</code><br>
  <code>PANTS_PEX_VERBOSITY</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>0</code></span>

<br>

Set the verbosity level of PEX logging, from 0 (no logging) up to 9 (max logging).
</div>
<br>

<div style="color: purple">

### `venv_use_symlinks`

  <code>--[no-]pex-venv-use-symlinks</code><br>
  <code>PANTS_PEX_VENV_USE_SYMLINKS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

When possible, use venvs whose site-packages directories are populated with symlinks.

Enabling this can save space in the `--named-caches-dir` directory and lead to slightly faster execution times for Pants Python goals. Some distributions do not work with symlinked venvs though, so you may not be able to enable this optimization as a result.
</div>
<br>

<div style="color: purple">

### `executable_search_paths`

  <code>--pex-executable-search-paths=&quot;[&lt;binary-paths&gt;, &lt;binary-paths&gt;, ...]&quot;</code><br>
  <code>PANTS_PEX_EXECUTABLE_SEARCH_PATHS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "&lt;PATH&gt;"
]</pre></span>

<br>

The PATH value that will be used by the PEX subprocess and any subprocesses it spawns.

The special string `"<PATH>"` will expand to the contents of the PATH env var.

Can be overriden by field `pex_executable_search_paths` on `local_environment`, `docker_environment`, or `remote_environment` targets.
</div>
<br>


## Deprecated options

None


