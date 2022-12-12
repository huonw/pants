
The Python import sorter tool (https://pycqa.github.io/isort/).

Backend: <span style="color: purple"><code>pants.backend.python.lint.isort</code></span>
Config section: <span style="color: purple"><code>[isort]</code></span>

## Basic options

<div style="color: purple">

### `skip`

  <code>--[no-]isort-skip</code><br>
  <code>PANTS_ISORT_SKIP</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

If true, don't use isort when running `./pants fmt` and `./pants lint`.
</div>
<br>

<div style="color: purple">

### `args`

  <code>--isort-args=&quot;[&lt;shell_str&gt;, &lt;shell_str&gt;, ...]&quot;</code><br>
  <code>PANTS_ISORT_ARGS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Arguments to pass directly to isort, e.g. `--isort-args='--case-sensitive --trailing-comma'`.
</div>
<br>


## Advanced options

<div style="color: purple">

### `version`

  <code>--isort-version=&lt;str&gt;</code><br>
  <code>PANTS_ISORT_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>isort[pyproject,colors]&gt;=5.9.3,&lt;6.0</code></span>

<br>

Requirement string for the tool.
</div>
<br>

<div style="color: purple">

### `extra_requirements`

  <code>--isort-extra-requirements=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_ISORT_EXTRA_REQUIREMENTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Any additional requirement strings to use with the tool. This is useful if the tool allows you to install plugins or if you need to constrain a dependency to a certain version.
</div>
<br>

<div style="color: purple">

### `interpreter_constraints`

  <code>--isort-interpreter-constraints=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_ISORT_INTERPRETER_CONSTRAINTS</code><br>
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

  <code>--isort-lockfile=&lt;str&gt;</code><br>
  <code>PANTS_ISORT_LOCKFILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;default&gt;</code></span>

<br>

Path to a lockfile used for installing the tool.

Set to the string `<default>` to use a lockfile provided by Pants, so long as you have not changed the `--version` and `--extra-requirements` options, and the tool's interpreter constraints are compatible with the default. Pants will error or warn if the lockfile is not compatible (controlled by `[python].invalid_lockfile_behavior`). See https://github.com/pantsbuild/pants/blob/release_2.16.0.dev2/src/python/pants/backend/python/lint/isort/isort.lock for the default lockfile contents.

Set to the string `<none>` to opt out of using a lockfile. We do not recommend this, though, as lockfiles are essential for reproducible builds and supply-chain security.

To use a custom lockfile, set this option to a file path relative to the build root, then run `./pants generate-lockfiles --resolve=isort`.

Alternatively, you can set this option to the path to a custom lockfile using pip's requirements.txt-style, ideally with `--hash`. Set `[python].invalid_lockfile_behavior = 'ignore'` so that Pants does not complain about missing lockfile headers.
</div>
<br>

<div style="color: purple">

### `console_script`

  <code>--isort-console-script=&lt;str&gt;</code><br>
  <code>PANTS_ISORT_CONSOLE_SCRIPT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>isort</code></span>

<br>

The console script for the tool. Using this option is generally preferable to (and mutually exclusive with) specifying an --entry-point since console script names have a higher expectation of staying stable across releases of the tool. Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `entry_point`

  <code>--isort-entry-point=&lt;str&gt;</code><br>
  <code>PANTS_ISORT_ENTRY_POINT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

The entry point for the tool. Generally you only want to use this option if the tool does not offer a --console-script (which this option is mutually exclusive with). Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `config`

  <code>--isort-config=&quot;[&lt;file_option&gt;, &lt;file_option&gt;, ...]&quot;</code><br>
  <code>PANTS_ISORT_CONFIG</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Path to config file understood by isort (https://pycqa.github.io/isort/docs/configuration/config_files/).

Setting this option will disable `[isort].config_discovery`. Use this option if the config is located in a non-standard location.

If using isort 5+ and you specify only 1 config file, Pants will configure isort's argv to point to your config file.
</div>
<br>

<div style="color: purple">

### `config_discovery`

  <code>--[no-]isort-config-discovery</code><br>
  <code>PANTS_ISORT_CONFIG_DISCOVERY</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>

<br>

If true, Pants will include any relevant config files during runs (`.isort.cfg`, `pyproject.toml`, `setup.cfg`, `tox.ini` and `.editorconfig`).

Use `[isort].config` instead if your config is in a non-standard location.
</div>
<br>


## Deprecated options

<div style="color: purple">

### `export`

  <code>--[no-]isort-export</code><br>
  <code>PANTS_ISORT_EXPORT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>
<p style="color: darkred">Deprecated, is scheduled to be removed in version: 2.23.0.dev0.<br>Use the export goal's --resolve option to select tools to export, instead of using this option to exempt a tool from export-by-default.</p>
<br>

If true, export a virtual environment with isort when running `./pants export`.

This can be useful, for example, with IDE integrations to point your editor to the tool's binary.
</div>
<br>



