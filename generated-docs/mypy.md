
The MyPy Python type checker (http://mypy-lang.org/).

Backend: <span style="color: purple"><code>pants.backend.python.typecheck.mypy</code></span>
Config section: <span style="color: purple"><code>[mypy]</code></span>

## Basic options

<div style="color: purple">

### `skip`

  <code>--[no-]mypy-skip</code><br>
  <code>PANTS_MYPY_SKIP</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

If true, don't use MyPy when running `./pants check`.
</div>
<br>

<div style="color: purple">

### `args`

  <code>--mypy-args=&quot;[&lt;shell_str&gt;, &lt;shell_str&gt;, ...]&quot;</code><br>
  <code>PANTS_MYPY_ARGS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Arguments to pass directly to MyPy, e.g. `--mypy-args='--python-version 3.7 --disallow-any-expr'`.
</div>
<br>


## Advanced options

<div style="color: purple">

### `version`

  <code>--mypy-version=&lt;str&gt;</code><br>
  <code>PANTS_MYPY_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>mypy==0.961</code></span>

<br>

Requirement string for the tool.
</div>
<br>

<div style="color: purple">

### `extra_requirements`

  <code>--mypy-extra-requirements=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_MYPY_EXTRA_REQUIREMENTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Any additional requirement strings to use with the tool. This is useful if the tool allows you to install plugins or if you need to constrain a dependency to a certain version.
</div>
<br>

<div style="color: purple">

### `interpreter_constraints`

  <code>--mypy-interpreter-constraints=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_MYPY_INTERPRETER_CONSTRAINTS</code><br>
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

  <code>--mypy-lockfile=&lt;str&gt;</code><br>
  <code>PANTS_MYPY_LOCKFILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;default&gt;</code></span>

<br>

Path to a lockfile used for installing the tool.

Set to the string `<default>` to use a lockfile provided by Pants, so long as you have not changed the `--version` and `--extra-requirements` options, and the tool's interpreter constraints are compatible with the default. Pants will error or warn if the lockfile is not compatible (controlled by `[python].invalid_lockfile_behavior`). See https://github.com/pantsbuild/pants/blob/release_2.16.0.dev2/src/python/pants/backend/python/typecheck/mypy/mypy.lock for the default lockfile contents.

Set to the string `<none>` to opt out of using a lockfile. We do not recommend this, though, as lockfiles are essential for reproducible builds and supply-chain security.

To use a custom lockfile, set this option to a file path relative to the build root, then run `./pants generate-lockfiles --resolve=mypy`.

Alternatively, you can set this option to the path to a custom lockfile using pip's requirements.txt-style, ideally with `--hash`. Set `[python].invalid_lockfile_behavior = 'ignore'` so that Pants does not complain about missing lockfile headers.
</div>
<br>

<div style="color: purple">

### `console_script`

  <code>--mypy-console-script=&lt;str&gt;</code><br>
  <code>PANTS_MYPY_CONSOLE_SCRIPT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>mypy</code></span>

<br>

The console script for the tool. Using this option is generally preferable to (and mutually exclusive with) specifying an --entry-point since console script names have a higher expectation of staying stable across releases of the tool. Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `entry_point`

  <code>--mypy-entry-point=&lt;str&gt;</code><br>
  <code>PANTS_MYPY_ENTRY_POINT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

The entry point for the tool. Generally you only want to use this option if the tool does not offer a --console-script (which this option is mutually exclusive with). Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `config`

  <code>--mypy-config=&lt;file_option&gt;</code><br>
  <code>PANTS_MYPY_CONFIG</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

Path to a config file understood by MyPy (https://mypy.readthedocs.io/en/stable/config_file.html).

Setting this option will disable `[mypy].config_discovery`. Use this option if the config is located in a non-standard location.
</div>
<br>

<div style="color: purple">

### `config_discovery`

  <code>--[no-]mypy-config-discovery</code><br>
  <code>PANTS_MYPY_CONFIG_DISCOVERY</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>

<br>

If true, Pants will include any relevant config files during runs (`mypy.ini`, `.mypy.ini`, and `setup.cfg`).

Use `[mypy].config` instead if your config is in a non-standard location.
</div>
<br>

<div style="color: purple">

### `source_plugins`

  <code>--mypy-source-plugins=&quot;[&lt;target_option&gt;, &lt;target_option&gt;, ...]&quot;</code><br>
  <code>PANTS_MYPY_SOURCE_PLUGINS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

An optional list of `python_sources` target addresses to load first-party plugins.

You must also set `plugins = path.to.module` in your `mypy.ini`, and set the `[mypy].config` option in your `pants.toml`.

To instead load third-party plugins, set the option `[mypy].extra_requirements` and set the `plugins` option in `mypy.ini`. Tip: it's often helpful to define a dedicated 'resolve' via `[python].resolves` for your MyPy plugins such as 'mypy-plugins' so that the third-party requirements used by your plugin, like `mypy`, do not mix with the rest of your project. Read that option's help message for more info on resolves.
</div>
<br>

<div style="color: purple">

### `extra_type_stubs`

  <code>--mypy-extra-type-stubs=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_MYPY_EXTRA_TYPE_STUBS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Extra type stub requirements to install when running MyPy.

Normally, type stubs can be installed as typical requirements, such as putting them in `requirements.txt` or using a `python_requirement` target. Alternatively, you can use this option so that the dependencies are solely used when running MyPy and are not runtime dependencies.

Expects a list of pip-style requirement strings, like `['types-requests==2.25.9']`.

We recommend also enabling `[mypy].extra_type_stubs_lockfile` for a more reproducible build and less supply-chain security risk.
</div>
<br>

<div style="color: purple">

### `extra_type_stubs_lockfile`

  <code>--mypy-extra-type-stubs-lockfile=&lt;str&gt;</code><br>
  <code>PANTS_MYPY_EXTRA_TYPE_STUBS_LOCKFILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;none&gt;</code></span>

<br>

Path to a lockfile for the option `[mypy].extra_type_stubs`.

Set to the string `<none>` to opt out of using a lockfile. We do not recommend this if you use `[mypy].extra_type_stubs`, though, as lockfiles are essential for reproducible builds and supply-chain security.

To use a lockfile, set this option to a file path relative to the build root, then run `./pants generate-lockfiles --resolve=mypy-extra-type-stubs`.
</div>
<br>


## Deprecated options

<div style="color: purple">

### `export`

  <code>--[no-]mypy-export</code><br>
  <code>PANTS_MYPY_EXPORT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>
<p style="color: darkred">Deprecated, is scheduled to be removed in version: 2.23.0.dev0.<br>Use the export goal's --resolve option to select tools to export, instead of using this option to exempt a tool from export-by-default.</p>
<br>

If true, export a virtual environment with MyPy when running `./pants export`.

This can be useful, for example, with IDE integrations to point your editor to the tool's binary.
</div>
<br>



