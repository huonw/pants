
Used perform modifications to the final output produced by Helm charts when they've been fully rendered.

Backend: <span style="color: purple"><code>pants.backend.experimental.helm</code></span>
Config section: <span style="color: purple"><code>[helm-post-renderer]</code></span>

## Basic options

None

## Advanced options

<div style="color: purple">

### `version`

  <code>--helm-post-renderer-version=&lt;str&gt;</code><br>
  <code>PANTS_HELM_POST_RENDERER_VERSION</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>yamlpath&gt;=3.6,&lt;3.7</code></span>

<br>

Requirement string for the tool.
</div>
<br>

<div style="color: purple">

### `extra_requirements`

  <code>--helm-post-renderer-extra-requirements=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_HELM_POST_RENDERER_EXTRA_REQUIREMENTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "ruamel.yaml&gt;=0.15.96,!=0.17.0,!=0.17.1,!=0.17.2,!=0.17.5,&lt;=0.17.21"
]</pre></span>

<br>

Any additional requirement strings to use with the tool. This is useful if the tool allows you to install plugins or if you need to constrain a dependency to a certain version.
</div>
<br>

<div style="color: purple">

### `interpreter_constraints`

  <code>--helm-post-renderer-interpreter-constraints=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_HELM_POST_RENDERER_INTERPRETER_CONSTRAINTS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "CPython&gt;=3.7,&lt;3.10"
]</pre></span>

<br>

Python interpreter constraints for this tool.
</div>
<br>

<div style="color: purple">

### `lockfile`

  <code>--helm-post-renderer-lockfile=&lt;str&gt;</code><br>
  <code>PANTS_HELM_POST_RENDERER_LOCKFILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>&lt;default&gt;</code></span>

<br>

Path to a lockfile used for installing the tool.

Set to the string `<default>` to use a lockfile provided by Pants, so long as you have not changed the `--version` and `--extra-requirements` options, and the tool's interpreter constraints are compatible with the default. Pants will error or warn if the lockfile is not compatible (controlled by `[python].invalid_lockfile_behavior`). See https://github.com/pantsbuild/pants/blob/release_2.16.0.dev2/src/python/pants/backend/helm/subsystems/post_renderer.lock for the default lockfile contents.

Set to the string `<none>` to opt out of using a lockfile. We do not recommend this, though, as lockfiles are essential for reproducible builds and supply-chain security.

To use a custom lockfile, set this option to a file path relative to the build root, then run `./pants generate-lockfiles --resolve=helm-post-renderer`.

Alternatively, you can set this option to the path to a custom lockfile using pip's requirements.txt-style, ideally with `--hash`. Set `[python].invalid_lockfile_behavior = 'ignore'` so that Pants does not complain about missing lockfile headers.
</div>
<br>


## Deprecated options

None


