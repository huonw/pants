
Upgrade syntax for newer versions of the language (https://github.com/asottile/pyupgrade).

Backend: <span style="color: purple"><code>pants.backend.experimental.python.lint.pyupgrade</code></span>
Config section: <span style="color: purple"><code>[pyupgrade]</code></span>

## Basic options

<div style="color: purple">

### `skip`

  <code>--[no-]pyupgrade-skip</code><br>
  <code>PANTS_PYUPGRADE_SKIP</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

If true, don't use pyupgrade when running `./pants fmt` and `./pants lint`.
</div>
<br>

<div style="color: purple">

### `args`

  <code>--pyupgrade-args=&quot;[&lt;shell_str&gt;, &lt;shell_str&gt;, ...]&quot;</code><br>
  <code>PANTS_PYUPGRADE_ARGS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Arguments to pass directly to pyupgrade, e.g. `--pyupgrade-args='--py39-plus --keep-runtime-typing'`.
</div>
<br>


## Advanced options

<div style="color: purple">

### `version`

  <code>--pyupgrade-version=&lt;str&gt;</code><br>
  <code>PANTS_PYUPGRADE_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>pyupgrade&gt;=2.33.0,&lt;2.35</code></span>

<br>

Requirement string for the tool.
</div>
<br>

<div style="color: purple">

### `extra_requirements`

  <code>--pyupgrade-extra-requirements=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_PYUPGRADE_EXTRA_REQUIREMENTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Any additional requirement strings to use with the tool. This is useful if the tool allows you to install plugins or if you need to constrain a dependency to a certain version.
</div>
<br>

<div style="color: purple">

### `interpreter_constraints`

  <code>--pyupgrade-interpreter-constraints=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_PYUPGRADE_INTERPRETER_CONSTRAINTS</code><br>
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

  <code>--pyupgrade-lockfile=&lt;str&gt;</code><br>
  <code>PANTS_PYUPGRADE_LOCKFILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;default&gt;</code></span>

<br>

Path to a lockfile used for installing the tool.

Set to the string `<default>` to use a lockfile provided by Pants, so long as you have not changed the `--version` and `--extra-requirements` options, and the tool's interpreter constraints are compatible with the default. Pants will error or warn if the lockfile is not compatible (controlled by `[python].invalid_lockfile_behavior`). See https://github.com/pantsbuild/pants/blob/release_2.16.0.dev2/src/python/pants/backend/python/lint/pyupgrade/pyupgrade.lock for the default lockfile contents.

Set to the string `<none>` to opt out of using a lockfile. We do not recommend this, though, as lockfiles are essential for reproducible builds and supply-chain security.

To use a custom lockfile, set this option to a file path relative to the build root, then run `./pants generate-lockfiles --resolve=pyupgrade`.

Alternatively, you can set this option to the path to a custom lockfile using pip's requirements.txt-style, ideally with `--hash`. Set `[python].invalid_lockfile_behavior = 'ignore'` so that Pants does not complain about missing lockfile headers.
</div>
<br>

<div style="color: purple">

### `console_script`

  <code>--pyupgrade-console-script=&lt;str&gt;</code><br>
  <code>PANTS_PYUPGRADE_CONSOLE_SCRIPT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>pyupgrade</code></span>

<br>

The console script for the tool. Using this option is generally preferable to (and mutually exclusive with) specifying an --entry-point since console script names have a higher expectation of staying stable across releases of the tool. Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `entry_point`

  <code>--pyupgrade-entry-point=&lt;str&gt;</code><br>
  <code>PANTS_PYUPGRADE_ENTRY_POINT</code><br>
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

  <code>--[no-]pyupgrade-export</code><br>
  <code>PANTS_PYUPGRADE_EXPORT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>
<p style="color: darkred">Deprecated, is scheduled to be removed in version: 2.23.0.dev0.<br>Use the export goal's --resolve option to select tools to export, instead of using this option to exempt a tool from export-by-default.</p>
<br>

If true, export a virtual environment with pyupgrade when running `./pants export`.

This can be useful, for example, with IDE integrations to point your editor to the tool's binary.
</div>
<br>



