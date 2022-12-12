
The IPython enhanced REPL (https://ipython.org/).

Backend: <span style="color: purple"><code>pants.backend.python</code></span>
Config section: <span style="color: purple"><code>[ipython]</code></span>

## Basic options

None

## Advanced options

<div style="color: purple">

### `version`

  <code>--ipython-version=&lt;str&gt;</code><br>
  <code>PANTS_IPYTHON_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>ipython&gt;=7.34,&lt;8</code></span>

<br>

Requirement string for the tool.
</div>
<br>

<div style="color: purple">

### `extra_requirements`

  <code>--ipython-extra-requirements=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_IPYTHON_EXTRA_REQUIREMENTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Any additional requirement strings to use with the tool. This is useful if the tool allows you to install plugins or if you need to constrain a dependency to a certain version.
</div>
<br>

<div style="color: purple">

### `lockfile`

  <code>--ipython-lockfile=&lt;str&gt;</code><br>
  <code>PANTS_IPYTHON_LOCKFILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;default&gt;</code></span>

<br>

Path to a lockfile used for installing the tool.

Set to the string `<default>` to use a lockfile provided by Pants, so long as you have not changed the `--version` and `--extra-requirements` options, and the tool's interpreter constraints are compatible with the default. Pants will error or warn if the lockfile is not compatible (controlled by `[python].invalid_lockfile_behavior`). See https://github.com/pantsbuild/pants/blob/release_2.16.0.dev2/src/python/pants/backend/python/subsystems/ipython.lock for the default lockfile contents.

Set to the string `<none>` to opt out of using a lockfile. We do not recommend this, though, as lockfiles are essential for reproducible builds and supply-chain security.

To use a custom lockfile, set this option to a file path relative to the build root, then run `./pants generate-lockfiles --resolve=ipython`.

Alternatively, you can set this option to the path to a custom lockfile using pip's requirements.txt-style, ideally with `--hash`. Set `[python].invalid_lockfile_behavior = 'ignore'` so that Pants does not complain about missing lockfile headers.
</div>
<br>

<div style="color: purple">

### `console_script`

  <code>--ipython-console-script=&lt;str&gt;</code><br>
  <code>PANTS_IPYTHON_CONSOLE_SCRIPT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>ipython</code></span>

<br>

The console script for the tool. Using this option is generally preferable to (and mutually exclusive with) specifying an --entry-point since console script names have a higher expectation of staying stable across releases of the tool. Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `entry_point`

  <code>--ipython-entry-point=&lt;str&gt;</code><br>
  <code>PANTS_IPYTHON_ENTRY_POINT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

The entry point for the tool. Generally you only want to use this option if the tool does not offer a --console-script (which this option is mutually exclusive with). Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `ignore_cwd`

  <code>--[no-]ipython-ignore-cwd</code><br>
  <code>PANTS_IPYTHON_IGNORE_CWD</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>

<br>

Whether to tell IPython not to put the CWD on the import path.

Normally you want this to be True, so that imports come from the hermetic environment Pants creates.

However IPython<7.13.0 doesn't support this option, so if you're using an earlier version (e.g., because you have Python 2.7 code) then you will need to set this to False, and you may have issues with imports from your CWD shading the hermetic environment.
</div>
<br>


## Deprecated options

None


