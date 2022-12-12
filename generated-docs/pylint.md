
The Pylint linter for Python code (https://www.pylint.org/).

Backend: <span style="color: purple"><code>pants.backend.python.lint.pylint</code></span>
Config section: <span style="color: purple"><code>[pylint]</code></span>

## Basic options

<div style="color: purple">

### `skip`

  <code>--[no-]pylint-skip</code><br>
  <code>PANTS_PYLINT_SKIP</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

If true, don't use Pylint when running `./pants lint`.
</div>
<br>

<div style="color: purple">

### `args`

  <code>--pylint-args=&quot;[&lt;shell_str&gt;, &lt;shell_str&gt;, ...]&quot;</code><br>
  <code>PANTS_PYLINT_ARGS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Arguments to pass directly to Pylint, e.g. `--pylint-args='--ignore=foo.py,bar.py --disable=C0330,W0311'`.
</div>
<br>


## Advanced options

<div style="color: purple">

### `version`

  <code>--pylint-version=&lt;str&gt;</code><br>
  <code>PANTS_PYLINT_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>pylint&gt;=2.13.0,&lt;2.15</code></span>

<br>

Requirement string for the tool.
</div>
<br>

<div style="color: purple">

### `extra_requirements`

  <code>--pylint-extra-requirements=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_PYLINT_EXTRA_REQUIREMENTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Any additional requirement strings to use with the tool. This is useful if the tool allows you to install plugins or if you need to constrain a dependency to a certain version.
</div>
<br>

<div style="color: purple">

### `lockfile`

  <code>--pylint-lockfile=&lt;str&gt;</code><br>
  <code>PANTS_PYLINT_LOCKFILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;default&gt;</code></span>

<br>

Path to a lockfile used for installing the tool.

Set to the string `<default>` to use a lockfile provided by Pants, so long as you have not changed the `--version` and `--extra-requirements` options, and the tool's interpreter constraints are compatible with the default. Pants will error or warn if the lockfile is not compatible (controlled by `[python].invalid_lockfile_behavior`). See https://github.com/pantsbuild/pants/blob/release_2.16.0.dev2/src/python/pants/backend/python/lint/pylint/pylint.lock for the default lockfile contents.

Set to the string `<none>` to opt out of using a lockfile. We do not recommend this, though, as lockfiles are essential for reproducible builds and supply-chain security.

To use a custom lockfile, set this option to a file path relative to the build root, then run `./pants generate-lockfiles --resolve=pylint`.

Alternatively, you can set this option to the path to a custom lockfile using pip's requirements.txt-style, ideally with `--hash`. Set `[python].invalid_lockfile_behavior = 'ignore'` so that Pants does not complain about missing lockfile headers.
</div>
<br>

<div style="color: purple">

### `console_script`

  <code>--pylint-console-script=&lt;str&gt;</code><br>
  <code>PANTS_PYLINT_CONSOLE_SCRIPT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>pylint</code></span>

<br>

The console script for the tool. Using this option is generally preferable to (and mutually exclusive with) specifying an --entry-point since console script names have a higher expectation of staying stable across releases of the tool. Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `entry_point`

  <code>--pylint-entry-point=&lt;str&gt;</code><br>
  <code>PANTS_PYLINT_ENTRY_POINT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

The entry point for the tool. Generally you only want to use this option if the tool does not offer a --console-script (which this option is mutually exclusive with). Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `config`

  <code>--pylint-config=&lt;file_option&gt;</code><br>
  <code>PANTS_PYLINT_CONFIG</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

Path to a config file understood by Pylint (http://pylint.pycqa.org/en/latest/user_guide/run.html#command-line-options).

Setting this option will disable `[pylint].config_discovery`. Use this option if the config is located in a non-standard location.
</div>
<br>

<div style="color: purple">

### `config_discovery`

  <code>--[no-]pylint-config-discovery</code><br>
  <code>PANTS_PYLINT_CONFIG_DISCOVERY</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>

<br>

If true, Pants will include any relevant config files during runs (`.pylintrc`, `pylintrc`, `pyproject.toml`, and `setup.cfg`).

Use `[pylint].config` instead if your config is in a non-standard location.
</div>
<br>

<div style="color: purple">

### `source_plugins`

  <code>--pylint-source-plugins=&quot;[&lt;target_option&gt;, &lt;target_option&gt;, ...]&quot;</code><br>
  <code>PANTS_PYLINT_SOURCE_PLUGINS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

An optional list of `python_sources` target addresses to load first-party plugins.

You must set the plugin's parent directory as a source root. For example, if your plugin is at `build-support/pylint/custom_plugin.py`, add 'build-support/pylint' to `[source].root_patterns` in `pants.toml`. This is necessary for Pants to know how to tell Pylint to discover your plugin. See https://www.pantsbuild.org/v2.16/docs/source-roots

You must also set `load-plugins=$module_name` in your Pylint config file.

While your plugin's code can depend on other first-party code and third-party requirements, all first-party dependencies of the plugin must live in the same directory or a subdirectory.

To instead load third-party plugins, set the option `[pylint].extra_requirements` and set the `load-plugins` option in your Pylint config.

Tip: it's often helpful to define a dedicated 'resolve' via `[python].resolves` for your Pylint plugins such as 'pylint-plugins' so that the third-party requirements used by your plugin, like `pylint`, do not mix with the rest of your project. Read that option's help message for more info on resolves.
</div>
<br>


## Deprecated options

<div style="color: purple">

### `export`

  <code>--[no-]pylint-export</code><br>
  <code>PANTS_PYLINT_EXPORT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>
<p style="color: darkred">Deprecated, is scheduled to be removed in version: 2.23.0.dev0.<br>Use the export goal's --resolve option to select tools to export, instead of using this option to exempt a tool from export-by-default.</p>
<br>

If true, export a virtual environment with Pylint when running `./pants export`.

This can be useful, for example, with IDE integrations to point your editor to the tool's binary.
</div>
<br>



