
The add-trailing-comma Python code formatter (https://github.com/asottile/add-trailing-comma).

Backend: <span style="color: purple"><code>pants.backend.experimental.python.lint.add_trailing_comma</code></span>
Config section: <span style="color: purple"><code>[add-trailing-comma]</code></span>

## Basic options

<div style="color: purple">

### `skip`

  <code>--[no-]add-trailing-comma-skip</code><br>
  <code>PANTS_ADD_TRAILING_COMMA_SKIP</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

If true, don't use add-trailing-comma when running `./pants fmt` and `./pants lint`.
</div>
<br>

<div style="color: purple">

### `args`

  <code>--add-trailing-comma-args=&quot;[&lt;shell_str&gt;, &lt;shell_str&gt;, ...]&quot;</code><br>
  <code>PANTS_ADD_TRAILING_COMMA_ARGS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Arguments to pass directly to add-trailing-comma, e.g. `--add-trailing-comma-args='--py36-plus'`.
</div>
<br>


## Advanced options

<div style="color: purple">

### `version`

  <code>--add-trailing-comma-version=&lt;str&gt;</code><br>
  <code>PANTS_ADD_TRAILING_COMMA_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>add-trailing-comma==2.2.3</code></span>

<br>

Requirement string for the tool.
</div>
<br>

<div style="color: purple">

### `extra_requirements`

  <code>--add-trailing-comma-extra-requirements=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_ADD_TRAILING_COMMA_EXTRA_REQUIREMENTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Any additional requirement strings to use with the tool. This is useful if the tool allows you to install plugins or if you need to constrain a dependency to a certain version.
</div>
<br>

<div style="color: purple">

### `interpreter_constraints`

  <code>--add-trailing-comma-interpreter-constraints=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_ADD_TRAILING_COMMA_INTERPRETER_CONSTRAINTS</code><br>
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

  <code>--add-trailing-comma-lockfile=&lt;str&gt;</code><br>
  <code>PANTS_ADD_TRAILING_COMMA_LOCKFILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;default&gt;</code></span>

<br>

Path to a lockfile used for installing the tool.

Set to the string `<default>` to use a lockfile provided by Pants, so long as you have not changed the `--version` and `--extra-requirements` options, and the tool's interpreter constraints are compatible with the default. Pants will error or warn if the lockfile is not compatible (controlled by `[python].invalid_lockfile_behavior`). See https://github.com/pantsbuild/pants/blob/release_2.16.0.dev2/src/python/pants/backend/python/lint/add_trailing_comma/add_trailing_comma.lock for the default lockfile contents.

Set to the string `<none>` to opt out of using a lockfile. We do not recommend this, though, as lockfiles are essential for reproducible builds and supply-chain security.

To use a custom lockfile, set this option to a file path relative to the build root, then run `./pants generate-lockfiles --resolve=add-trailing-comma`.

Alternatively, you can set this option to the path to a custom lockfile using pip's requirements.txt-style, ideally with `--hash`. Set `[python].invalid_lockfile_behavior = 'ignore'` so that Pants does not complain about missing lockfile headers.
</div>
<br>

<div style="color: purple">

### `console_script`

  <code>--add-trailing-comma-console-script=&lt;str&gt;</code><br>
  <code>PANTS_ADD_TRAILING_COMMA_CONSOLE_SCRIPT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>add-trailing-comma</code></span>

<br>

The console script for the tool. Using this option is generally preferable to (and mutually exclusive with) specifying an --entry-point since console script names have a higher expectation of staying stable across releases of the tool. Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `entry_point`

  <code>--add-trailing-comma-entry-point=&lt;str&gt;</code><br>
  <code>PANTS_ADD_TRAILING_COMMA_ENTRY_POINT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

The entry point for the tool. Generally you only want to use this option if the tool does not offer a --console-script (which this option is mutually exclusive with). Usually, you will not want to change this from the default.
</div>
<br>


## Deprecated options

<div style="color: purple">

### `export`

  <code>--[no-]add-trailing-comma-export</code><br>
  <code>PANTS_ADD_TRAILING_COMMA_EXPORT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>
<p style="color: darkred">Deprecated, is scheduled to be removed in version: 2.23.0.dev0.<br>Use the export goal's --resolve option to select tools to export, instead of using this option to exempt a tool from export-by-default.</p>
<br>

If true, export a virtual environment with add-trailing-comma when running `./pants export`.

This can be useful, for example, with IDE integrations to point your editor to the tool's binary.
</div>
<br>



