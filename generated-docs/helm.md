
The Helm command line (https://helm.sh)

Backend: <span style="color: purple"><code>pants.backend.experimental.helm</code></span>
Config section: <span style="color: purple"><code>[helm]</code></span>

## Basic options

<div style="color: purple">

### `registries`

  <code>--helm-registries=&quot;{'key1': val1, 'key2': val2, ...}&quot;</code><br>
  <code>PANTS_HELM_REGISTRIES</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>{}</code></span>

<br>

Configure Helm OCI registries. The schema for a registry entry is as follows:

    {
        "registry-alias": {
            "address": "oci://registry-domain:port",
            "default": bool,
        },
        ...
    }

If no registries are provided in either a `helm_chart` target, then all default addresses will be used, if any.

The `helm_chart.registries` may be provided with a list of registry addresses and registry alias prefixed with `@` to be used instead of the defaults.

A configured registry is marked as default either by setting `default = true` or with an alias of `"default"`.

Registries also participate in resolving third party Helm charts uplodaded to those registries.
</div>
<br>

<div style="color: purple">

### `lint_strict`

  <code>--[no-]helm-lint-strict</code><br>
  <code>PANTS_HELM_LINT_STRICT</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

Enables strict linting of Helm charts
</div>
<br>

<div style="color: purple">

### `default_registry_repository`

  <code>--helm-default-registry-repository=&lt;str&gt;</code><br>
  <code>PANTS_HELM_DEFAULT_REGISTRY_REPOSITORY</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

Default location where to push Helm charts in the available registries when no specific one has been given.

If no registry repository is given, charts will be pushed to the root of the OCI registry.
</div>
<br>

<div style="color: purple">

### `args`

  <code>--helm-args=&quot;[&lt;shell_str&gt;, &lt;shell_str&gt;, ...]&quot;, ... -- [&lt;shell_str&gt; [&lt;shell_str&gt; [...]]]</code><br>
  <code>PANTS_HELM_ARGS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Arguments to pass directly to helmsubsystem, e.g. `--helm-args='--dry-run'`.

Additional arguments to pass to Helm command line.

Only a subset of Helm arguments are considered valid as passthrough arguments as most of them have equivalents in the form of fields of the different target types.

The list of valid arguments is as folows:

  * --atomic
  * --cleanup-on-fail
  * --debug
  * --dry-run
  * --force
  * --wait
  * --wait-for-jobs
  * --kubeconfig
  * --kube-context
  * --kube-apiserver
  * --kube-as-group
  * --kube-as-user
  * --kube-ca-file
  * --kube-token

Before attempting to use passthrough arguments, check the refence of each of the available target types to see what fields are accepted in each of them.
</div>
<br>


## Advanced options

<div style="color: purple">

### `version`

  <code>--helm-version=&lt;str&gt;</code><br>
  <code>PANTS_HELM_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>3.10.0</code></span>

<br>

Use this version of helmsubsystem.
</div>
<br>

<div style="color: purple">

### `known_versions`

  <code>--helm-known-versions=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_HELM_KNOWN_VERSIONS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "3.10.0|linux&lowbar;arm64 |3b72f5f8a60772fb156d0a4ab93272e8da7ef4d18e6421a7020d7c019f521fc1|13055719",
  "3.10.0|linux&lowbar;x86&lowbar;64|bf56beb418bb529b5e0d6d43d56654c5a03f89c98400b409d1013a33d9586474|14530566",
  "3.10.0|macos&lowbar;arm64 |f7f6558ebc8211824032a7fdcf0d55ad064cb33ec1eeec3d18057b9fe2e04dbe|14446277",
  "3.10.0|macos&lowbar;x86&lowbar;64|1e7fd528482ac2ef2d79fe300724b3e07ff6f846a2a9b0b0fe6f5fa05691786b|15237557",
  "3.8.0|linux&lowbar;arm64 |23e08035dc0106fe4e0bd85800fd795b2b9ecd9f32187aa16c49b0a917105161|12324642",
  "3.8.0|linux&lowbar;x86&lowbar;64|8408c91e846c5b9ba15eb6b1a5a79fc22dd4d33ac6ea63388e5698d1b2320c8b|13626774",
  "3.8.0|macos&lowbar;arm64 |751348f1a4a876ffe089fd68df6aea310fd05fe3b163ab76aa62632e327122f3|14078604",
  "3.8.0|macos&lowbar;x86&lowbar;64|532ddd6213891084873e5c2dcafa577f425ca662a6594a3389e288fc48dc2089|14318316"
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

  <code>--helm-use-unsupported-version=&lt;UnsupportedVersionUsage&gt;</code><br>
  <code>PANTS_HELM_USE_UNSUPPORTED_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">one of: <code>error, warning</code></span><br>
<span style="color: green">default: <code>error</code></span>

<br>


What action to take in case the requested version of helmsubsystem is not supported.

Supported helmsubsystem versions: unspecified

</div>
<br>

<div style="color: purple">

### `url_template`

  <code>--helm-url-template=&lt;str&gt;</code><br>
  <code>PANTS_HELM_URL_TEMPLATE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>https://get.helm.sh/helm-v{version}-{platform}.tar.gz</code></span>

<br>

URL to download the tool, either as a single binary file or a compressed file (e.g. zip file). You can change this to point to your own hosted file, e.g. to work with proxies or for access via the filesystem through a `file:$abspath` URL (e.g. `file:/this/is/absolute`, possibly by [templating the buildroot in a config file](https://www.pantsbuild.org/v2.16/docs/options#config-file-entries)).

Use `{version}` to have the value from --version substituted, and `{platform}` to have a value from --url-platform-mapping substituted in, depending on the current platform. For example, https://github.com/.../protoc-{version}-{platform}.zip.
</div>
<br>

<div style="color: purple">

### `url_platform_mapping`

  <code>--helm-url-platform-mapping=&quot;{'key1': val1, 'key2': val2, ...}&quot;</code><br>
  <code>PANTS_HELM_URL_PLATFORM_MAPPING</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>{
  "linux&lowbar;arm64": "linux-arm64",
  "linux&lowbar;x86&lowbar;64": "linux-amd64",
  "macos&lowbar;arm64": "darwin-arm64",
  "macos&lowbar;x86&lowbar;64": "darwin-amd64"
}</pre></span>

<br>

A dictionary mapping platforms to strings to be used when generating the URL to download the tool.

In --url-template, anytime the `{platform}` string is used, Pants will determine the current platform, and substitute `{platform}` with the respective value from your dictionary.

For example, if you define `{"macos_x86_64": "apple-darwin", "linux_x86_64": "unknown-linux"}`, and run Pants on Linux with an intel architecture, then `{platform}` will be substituted in the --url-template option with unknown-linux.
</div>
<br>

<div style="color: purple">

### `extra_env_vars`

  <code>--helm-extra-env-vars=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_HELM_EXTRA_ENV_VARS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Additional environment variables that would be made available to all Helm processes or during value interpolation.
</div>
<br>

<div style="color: purple">

### `tailor`

  <code>--[no-]helm-tailor</code><br>
  <code>PANTS_HELM_TAILOR</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>True</code></span>

<br>

If true, add `helm_chart` targets with the `tailor` goal.
</div>
<br>


## Deprecated options

None


