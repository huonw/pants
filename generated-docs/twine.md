
The utility for publishing Python distributions to PyPI and other Python repositories.

Backend: <span style="color: purple"><code>pants.backend.experimental.python</code></span>
Config section: <span style="color: purple"><code>[twine]</code></span>

## Basic options

<div style="color: purple">

### `skip`

  <code>--[no-]twine-skip</code><br>
  <code>PANTS_TWINE_SKIP</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

If true, don't use Twine when running `./pants publish`.
</div>
<br>

<div style="color: purple">

### `args`

  <code>--twine-args=&quot;[&lt;shell_str&gt;, &lt;shell_str&gt;, ...]&quot;</code><br>
  <code>PANTS_TWINE_ARGS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Arguments to pass directly to Twine, e.g. `--twine-args='--skip-existing'`.
</div>
<br>


## Advanced options

<div style="color: purple">

### `version`

  <code>--twine-version=&lt;str&gt;</code><br>
  <code>PANTS_TWINE_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>twine&gt;=3.7.1,&lt;3.8</code></span>

<br>

Requirement string for the tool.
</div>
<br>

<div style="color: purple">

### `extra_requirements`

  <code>--twine-extra-requirements=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_TWINE_EXTRA_REQUIREMENTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "colorama&gt;=0.4.3"
]</pre></span>

<br>

Any additional requirement strings to use with the tool. This is useful if the tool allows you to install plugins or if you need to constrain a dependency to a certain version.
</div>
<br>

<div style="color: purple">

### `interpreter_constraints`

  <code>--twine-interpreter-constraints=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_TWINE_INTERPRETER_CONSTRAINTS</code><br>
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

  <code>--twine-lockfile=&lt;str&gt;</code><br>
  <code>PANTS_TWINE_LOCKFILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;default&gt;</code></span>

<br>

Path to a lockfile used for installing the tool.

Set to the string `<default>` to use a lockfile provided by Pants, so long as you have not changed the `--version` and `--extra-requirements` options, and the tool's interpreter constraints are compatible with the default. Pants will error or warn if the lockfile is not compatible (controlled by `[python].invalid_lockfile_behavior`). See https://github.com/pantsbuild/pants/blob/release_2.16.0.dev2/src/python/pants/backend/python/subsystems/twine.lock for the default lockfile contents.

Set to the string `<none>` to opt out of using a lockfile. We do not recommend this, though, as lockfiles are essential for reproducible builds and supply-chain security.

To use a custom lockfile, set this option to a file path relative to the build root, then run `./pants generate-lockfiles --resolve=twine`.

Alternatively, you can set this option to the path to a custom lockfile using pip's requirements.txt-style, ideally with `--hash`. Set `[python].invalid_lockfile_behavior = 'ignore'` so that Pants does not complain about missing lockfile headers.
</div>
<br>

<div style="color: purple">

### `console_script`

  <code>--twine-console-script=&lt;str&gt;</code><br>
  <code>PANTS_TWINE_CONSOLE_SCRIPT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>twine</code></span>

<br>

The console script for the tool. Using this option is generally preferable to (and mutually exclusive with) specifying an --entry-point since console script names have a higher expectation of staying stable across releases of the tool. Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `entry_point`

  <code>--twine-entry-point=&lt;str&gt;</code><br>
  <code>PANTS_TWINE_ENTRY_POINT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

The entry point for the tool. Generally you only want to use this option if the tool does not offer a --console-script (which this option is mutually exclusive with). Usually, you will not want to change this from the default.
</div>
<br>

<div style="color: purple">

### `config`

  <code>--twine-config=&lt;file_option&gt;</code><br>
  <code>PANTS_TWINE_CONFIG</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

Path to a .pypirc config file to use. (https://packaging.python.org/specifications/pypirc/)

Setting this option will disable `[twine].config_discovery`. Use this option if the config is located in a non-standard location.
</div>
<br>

<div style="color: purple">

### `config_discovery`

  <code>--[no-]twine-config-discovery</code><br>
  <code>PANTS_TWINE_CONFIG_DISCOVERY</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>

<br>

If true, Pants will include all relevant config files during runs (`.pypirc`).

Use `[twine].config` instead if your config is in a non-standard location.
</div>
<br>

<div style="color: purple">

### `ca_certs_path`

  <code>--twine-ca-certs-path=&lt;str&gt;</code><br>
  <code>PANTS_TWINE_CA_CERTS_PATH</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;inherit&gt;</code></span>

<br>

Path to a file containing PEM-format CA certificates used for verifying secure connections when publishing python distributions.

Uses the value from `[GLOBAL].ca_certs_path` by default. Set to `"<none>"` to not use any certificates.

Even when using the `docker_environment` and `remote_environment` targets, this path will be read from the local host, and those certs will be used in the environment.

This option cannot be overridden via environment targets, so if you need a different value than what the rest of your organization is using, override the value via an environment variable, CLI argument, or `.pants.rc` file. See https://www.pantsbuild.org/v2.16/docs/options.
</div>
<br>


## Deprecated options

None


