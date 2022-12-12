
The pytest Python test framework (https://docs.pytest.org/).

Backend: <span style="color: purple"><code>pants.backend.python</code></span>
Config section: <span style="color: purple"><code>[pytest]</code></span>

## Basic options

<div style="color: purple">

### `args`

  <code>--pytest-args=&quot;[&lt;shell_str&gt;, &lt;shell_str&gt;, ...]&quot;, ... -- [&lt;shell_str&gt; [&lt;shell_str&gt; [...]]]</code><br>
  <code>PANTS_PYTEST_ARGS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Arguments to pass directly to Pytest, e.g. `--pytest-args='-k test_foo --quiet'`.
</div>
<br>

<div style="color: purple">

### `xdist_enabled`

  <code>--[no-]pytest-xdist-enabled</code><br>
  <code>PANTS_PYTEST_XDIST_ENABLED</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

If true, Pants will use `pytest-xdist` (https://pytest-xdist.readthedocs.io/en/latest/) to parallelize tests within each `python_test` target.

NOTE: Enabling `pytest-xdist` can cause high-level scoped fixtures (for example `session`) to execute more than once. See the `pytest-xdist` docs for more info: https://pypi.org/project/pytest-xdist/#making-session-scoped-fixtures-execute-only-once
</div>
<br>

<div style="color: purple">

### `skip`

  <code>--[no-]pytest-skip</code><br>
  <code>PANTS_PYTEST_SKIP</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

If true, don't use Pytest when running `./pants test`.
</div>
<br>


## Advanced options

<div style="color: purple">

### `version`

  <code>--pytest-version=&lt;str&gt;</code><br>
  <code>PANTS_PYTEST_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>pytest==7.0.1</code></span>

<br>

Requirement string for the tool.
</div>
<br>

<div style="color: purple">

### `extra_requirements`

  <code>--pytest-extra-requirements=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_PYTEST_EXTRA_REQUIREMENTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "pytest-cov&gt;=2.12,!=2.12.1,&lt;3.1",
  "pytest-xdist&gt;=2.5,&lt;3"
]</pre></span>

<br>

Any additional requirement strings to use with the tool. This is useful if the tool allows you to install plugins or if you need to constrain a dependency to a certain version.
</div>
<br>

<div style="color: purple">

### `lockfile`

  <code>--pytest-lockfile=&lt;str&gt;</code><br>
  <code>PANTS_PYTEST_LOCKFILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;default&gt;</code></span>

<br>

Path to a lockfile used for installing the tool.

Set to the string `<default>` to use a lockfile provided by Pants, so long as you have not changed the `--version` and `--extra-requirements` options, and the tool's interpreter constraints are compatible with the default. Pants will error or warn if the lockfile is not compatible (controlled by `[python].invalid_lockfile_behavior`). See https://github.com/pantsbuild/pants/blob/release_2.16.0.dev2/src/python/pants/backend/python/subsystems/pytest.lock for the default lockfile contents.

Set to the string `<none>` to opt out of using a lockfile. We do not recommend this, though, as lockfiles are essential for reproducible builds and supply-chain security.

To use a custom lockfile, set this option to a file path relative to the build root, then run `./pants generate-lockfiles --resolve=pytest`.

Alternatively, you can set this option to the path to a custom lockfile using pip's requirements.txt-style, ideally with `--hash`. Set `[python].invalid_lockfile_behavior = 'ignore'` so that Pants does not complain about missing lockfile headers.
</div>
<br>

<div style="color: purple">

### `console_script`

  <code>--pytest-console-script=&lt;str&gt;</code><br>
  <code>PANTS_PYTEST_CONSOLE_SCRIPT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>pytest</code></span>

<br>

The console script for the tool. Using this option is generally preferable to (and mutually exclusive with) specifying an --entry-point since console script names have a higher expectation of staying stable across releases of the tool. Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `entry_point`

  <code>--pytest-entry-point=&lt;str&gt;</code><br>
  <code>PANTS_PYTEST_ENTRY_POINT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

The entry point for the tool. Generally you only want to use this option if the tool does not offer a --console-script (which this option is mutually exclusive with). Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `junit_family`

  <code>--pytest-junit-family=&lt;str&gt;</code><br>
  <code>PANTS_PYTEST_JUNIT_FAMILY</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>xunit2</code></span>

<br>

The format of generated junit XML files. See https://docs.pytest.org/en/latest/reference.html#confval-junit_family.
</div>
<br>

<div style="color: purple">

### `execution_slot_var`

  <code>--pytest-execution-slot-var=&lt;str&gt;</code><br>
  <code>PANTS_PYTEST_EXECUTION_SLOT_VAR</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

If a non-empty string, the process execution slot id (an integer) will be exposed to tests under this environment variable name.
</div>
<br>

<div style="color: purple">

### `config`

  <code>--pytest-config=&lt;file_option&gt;</code><br>
  <code>PANTS_PYTEST_CONFIG</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

Path to a config file understood by Pytest (https://docs.pytest.org/en/latest/reference/customize.html#configuration-file-formats). Setting this option will disable `[pytest].config_discovery`. Use this option if the config is located in a non-standard location.
</div>
<br>

<div style="color: purple">

### `config_discovery`

  <code>--[no-]pytest-config-discovery</code><br>
  <code>PANTS_PYTEST_CONFIG_DISCOVERY</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>

<br>

If true, Pants will include all relevant Pytest config files (e.g. `pytest.ini`) during runs. See https://docs.pytest.org/en/stable/customize.html#finding-the-rootdir for where config files should be located for Pytest to discover them.

Use `[pytest].config` instead if your config is in a non-standard location.
</div>
<br>


## Deprecated options

<div style="color: purple">

### `export`

  <code>--[no-]pytest-export</code><br>
  <code>PANTS_PYTEST_EXPORT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>
<p style="color: darkred">Deprecated, is scheduled to be removed in version: 2.23.0.dev0.<br>Use the export goal's --resolve option to select tools to export, instead of using this option to exempt a tool from export-by-default.</p>
<br>

If true, export a virtual environment with Pytest when running `./pants export`.

This can be useful, for example, with IDE integrations to point your editor to the tool's binary.
</div>
<br>



