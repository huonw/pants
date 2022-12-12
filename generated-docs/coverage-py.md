
Configuration for Python test coverage measurement.

Backend: <span style="color: purple"><code>pants.backend.python</code></span>
Config section: <span style="color: purple"><code>[coverage-py]</code></span>

## Basic options

<div style="color: purple">

### `filter`

  <code>--coverage-py-filter=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_COVERAGE_PY_FILTER</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

A list of Python modules or filesystem paths to use in the coverage report, e.g. `['helloworld_test', 'helloworld/util/dirutil'].

Both modules and directory paths are recursive: any submodules or child paths, respectively, will be included.

If you leave this off, the coverage report will include every file in the transitive closure of the address/file arguments; for example, `test ::` will include every Python file in your project, whereas `test project/app_test.py` will include `app_test.py` and any of its transitive dependencies.
</div>
<br>

<div style="color: purple">

### `report`

  <code>--coverage-py-report=&quot;[&lt;CoverageReportType&gt;, &lt;CoverageReportType&gt;, ...]&quot;</code><br>
  <code>PANTS_COVERAGE_PY_REPORT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">one of: <code>console, xml, html, raw, json, lcov</code></span><br>
<span style="color: green">default: <pre>[
  "console"
]</pre></span>

<br>

Which coverage report type(s) to emit.
</div>
<br>

<div style="color: purple">

### `global_report`

  <code>--[no-]coverage-py-global-report</code><br>
  <code>PANTS_COVERAGE_PY_GLOBAL_REPORT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

If true, Pants will generate a global coverage report.

The global report will include all Python source files in the workspace and not just those depended on by the tests that were run.
</div>
<br>

<div style="color: purple">

### `fail_under`

  <code>--coverage-py-fail-under=&lt;float&gt;</code><br>
  <code>PANTS_COVERAGE_PY_FAIL_UNDER</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

Fail if the total combined coverage percentage for all tests is less than this number.

Use this instead of setting fail_under in a coverage.py config file, as the config will apply to each test separately, while you typically want this to apply to the combined coverage for all tests run.

Note that you must generate at least one (non-raw) coverage report for this check to trigger.

Note also that if you specify a non-integral value, you must also set [report] precision properly in the coverage.py config file to make use of the decimal places. See https://coverage.readthedocs.io/en/latest/config.html.
</div>
<br>


## Advanced options

<div style="color: purple">

### `version`

  <code>--coverage-py-version=&lt;str&gt;</code><br>
  <code>PANTS_COVERAGE_PY_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>coverage[toml]&gt;=6.5,&lt;6.6</code></span>

<br>

Requirement string for the tool.
</div>
<br>

<div style="color: purple">

### `extra_requirements`

  <code>--coverage-py-extra-requirements=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_COVERAGE_PY_EXTRA_REQUIREMENTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Any additional requirement strings to use with the tool. This is useful if the tool allows you to install plugins or if you need to constrain a dependency to a certain version.
</div>
<br>

<div style="color: purple">

### `interpreter_constraints`

  <code>--coverage-py-interpreter-constraints=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_COVERAGE_PY_INTERPRETER_CONSTRAINTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "CPython&gt;=3.7,&lt;4"
]</pre></span>

<br>

Python interpreter constraints for this tool.
</div>
<br>

<div style="color: purple">

### `lockfile`

  <code>--coverage-py-lockfile=&lt;str&gt;</code><br>
  <code>PANTS_COVERAGE_PY_LOCKFILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;default&gt;</code></span>

<br>

Path to a lockfile used for installing the tool.

Set to the string `<default>` to use a lockfile provided by Pants, so long as you have not changed the `--version` and `--extra-requirements` options, and the tool's interpreter constraints are compatible with the default. Pants will error or warn if the lockfile is not compatible (controlled by `[python].invalid_lockfile_behavior`). See https://github.com/pantsbuild/pants/blob/release_2.16.0.dev2/src/python/pants/backend/python/subsystems/coverage_py.lock for the default lockfile contents.

Set to the string `<none>` to opt out of using a lockfile. We do not recommend this, though, as lockfiles are essential for reproducible builds and supply-chain security.

To use a custom lockfile, set this option to a file path relative to the build root, then run `./pants generate-lockfiles --resolve=coverage-py`.

Alternatively, you can set this option to the path to a custom lockfile using pip's requirements.txt-style, ideally with `--hash`. Set `[python].invalid_lockfile_behavior = 'ignore'` so that Pants does not complain about missing lockfile headers.
</div>
<br>

<div style="color: purple">

### `console_script`

  <code>--coverage-py-console-script=&lt;str&gt;</code><br>
  <code>PANTS_COVERAGE_PY_CONSOLE_SCRIPT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>coverage</code></span>

<br>

The console script for the tool. Using this option is generally preferable to (and mutually exclusive with) specifying an --entry-point since console script names have a higher expectation of staying stable across releases of the tool. Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `entry_point`

  <code>--coverage-py-entry-point=&lt;str&gt;</code><br>
  <code>PANTS_COVERAGE_PY_ENTRY_POINT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

The entry point for the tool. Generally you only want to use this option if the tool does not offer a --console-script (which this option is mutually exclusive with). Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `output_dir`

  <code>--coverage-py-output-dir=&lt;str&gt;</code><br>
  <code>PANTS_COVERAGE_PY_OUTPUT_DIR</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>{distdir}/coverage/python</code></span>

<br>

Path to write the Pytest Coverage report to. Must be relative to the build root.
</div>
<br>

<div style="color: purple">

### `config`

  <code>--coverage-py-config=&lt;file_option&gt;</code><br>
  <code>PANTS_COVERAGE_PY_CONFIG</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

Path to an INI or TOML config file understood by coverage.py (https://coverage.readthedocs.io/en/stable/config.html).

Setting this option will disable `[coverage-py].config_discovery`. Use this option if the config is located in a non-standard location.
</div>
<br>

<div style="color: purple">

### `config_discovery`

  <code>--[no-]coverage-py-config-discovery</code><br>
  <code>PANTS_COVERAGE_PY_CONFIG_DISCOVERY</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>

<br>

If true, Pants will include any relevant config files during runs (`.coveragerc`, `setup.cfg`, `tox.ini`, and `pyproject.toml`).

Use `[coverage-py].config` instead if your config is in a non-standard location.
</div>
<br>


## Deprecated options

None


