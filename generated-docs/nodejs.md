
The NodeJS Javascript runtime (including npm and npx).

Backend: <span style="color: purple"><code>pants.backend.experimental.openapi.lint.spectral</code></span>
Config section: <span style="color: purple"><code>[nodejs]</code></span>

## Basic options

None

## Advanced options

<div style="color: purple">

### `version`

  <code>--nodejs-version=&lt;str&gt;</code><br>
  <code>PANTS_NODEJS_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>v16.15.0</code></span>

<br>

Use this version of nodejs.
</div>
<br>

<div style="color: purple">

### `known_versions`

  <code>--nodejs-known-versions=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_NODEJS_KNOWN_VERSIONS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "v16.15.0|macos&lowbar;arm64|ad8d8fc5330ef47788f509c2af398c8060bb59acbe914070d0df684cd2d8d39b|29126014",
  "v16.15.0|macos&lowbar;x86&lowbar;64|a6bb12bbf979d32137598e49d56d61bcddf8a8596c3442b44a9b3ace58dd4de8|30561503",
  "v16.15.0|linux&lowbar;arm64|b4080b86562c5397f32da7a0723b95b1df523cab4c757688a184e3f733a7df56|21403276",
  "v16.15.0|linux&lowbar;x86&lowbar;64|ebdf4dc9d992d19631f0931cca2fc33c6d0d382543639bc6560d31d5060a8372|22031988"
]</pre></span>

<br>


Known versions to verify downloads against.

Each element is a pipe-separated string of `version|platform|sha256|length`, where:

    - `version` is the version string
    - `platform` is one of [linux_arm64,linux_x86_64,macos_arm64,macos_x86_64],
    - `sha256` is the 64-character hex representation of the expected sha256
    digest of the download file, as emitted by `shasum -a 256`
    - `length` is the expected length of the download file in bytes, as emitted by
    `wc -c`

E.g., `3.1.2|macos_x86_64|6d0f18cd84b918c7b3edd0203e75569e0c7caecb1367bbbe409b44e28514f5be|42813`.

Values are space-stripped, so pipes can be indented for readability if necessary.

</div>
<br>

<div style="color: purple">

### `use_unsupported_version`

  <code>--nodejs-use-unsupported-version=&lt;UnsupportedVersionUsage&gt;</code><br>
  <code>PANTS_NODEJS_USE_UNSUPPORTED_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">one of: <code>error, warning</code></span><br>
<span style="color: green">default: <code>error</code></span>

<br>


What action to take in case the requested version of nodejs is not supported.

Supported nodejs versions: unspecified

</div>
<br>

<div style="color: purple">

### `url_template`

  <code>--nodejs-url-template=&lt;str&gt;</code><br>
  <code>PANTS_NODEJS_URL_TEMPLATE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>https://nodejs.org/dist/{version}/node-{version}-{platform}.tar</code></span>

<br>

URL to download the tool, either as a single binary file or a compressed file (e.g. zip file). You can change this to point to your own hosted file, e.g. to work with proxies or for access via the filesystem through a `file:$abspath` URL (e.g. `file:/this/is/absolute`, possibly by [templating the buildroot in a config file](https://www.pantsbuild.org/v2.16/docs/options#config-file-entries)).

Use `{version}` to have the value from --version substituted, and `{platform}` to have a value from --url-platform-mapping substituted in, depending on the current platform. For example, https://github.com/.../protoc-{version}-{platform}.zip.
</div>
<br>

<div style="color: purple">

### `url_platform_mapping`

  <code>--nodejs-url-platform-mapping=&quot;{'key1': val1, 'key2': val2, ...}&quot;</code><br>
  <code>PANTS_NODEJS_URL_PLATFORM_MAPPING</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>{
  "linux&lowbar;arm64": "linux-arm64",
  "linux&lowbar;x86&lowbar;64": "linux-x64",
  "macos&lowbar;arm64": "darwin-arm64",
  "macos&lowbar;x86&lowbar;64": "darwin-x64"
}</pre></span>

<br>

A dictionary mapping platforms to strings to be used when generating the URL to download the tool.

In --url-template, anytime the `{platform}` string is used, Pants will determine the current platform, and substitute `{platform}` with the respective value from your dictionary.

For example, if you define `{"macos_x86_64": "apple-darwin", "linux_x86_64": "unknown-linux"}`, and run Pants on Linux with an intel architecture, then `{platform}` will be substituted in the --url-template option with unknown-linux.
</div>
<br>


## Deprecated options

None


