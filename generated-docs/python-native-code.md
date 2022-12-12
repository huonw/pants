
Options for building native code using Python, e.g. when resolving distributions.

Backend: <span style="color: purple"><code>pants.backend.awslambda.python, pants.backend.codegen.protobuf.python, pants.backend.docker, pants.backend.docker.lint.hadolint, pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.helm, pants.backend.experimental.python, pants.backend.experimental.python.lint.add_trailing_comma, pants.backend.experimental.python.lint.autoflake, pants.backend.experimental.python.lint.pyupgrade, pants.backend.experimental.terraform, pants.backend.google_cloud_function.python, pants.backend.python, pants.backend.python.lint.bandit, pants.backend.python.lint.black, pants.backend.python.lint.docformatter, pants.backend.python.lint.flake8, pants.backend.python.lint.isort, pants.backend.python.lint.pylint, pants.backend.python.lint.yapf, pants.backend.python.typecheck.mypy, pants.core</code></span>
Config section: <span style="color: purple"><code>[python-native-code]</code></span>

## Basic options

None

## Advanced options

<div style="color: purple">

### `cpp_flags`

  <code>--python-native-code-cpp-flags=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_PYTHON_NATIVE_CODE_CPP_FLAGS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "&lt;CPPFLAGS&gt;"
]</pre></span>

<br>

Override the `CPPFLAGS` environment variable for any forked subprocesses. Use the value `['<CPPFLAGS>']` to inherit the value of the `CPPFLAGS` environment variable from your runtime environment target.

Can be overriden by field `python_native_code_cpp_flags` on `local_environment`, `docker_environment`, or `remote_environment` targets.
</div>
<br>

<div style="color: purple">

### `ld_flags`

  <code>--python-native-code-ld-flags=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_PYTHON_NATIVE_CODE_LD_FLAGS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "&lt;LDFLAGS&gt;"
]</pre></span>

<br>

Override the `LDFLAGS` environment variable for any forked subprocesses. Use the value `['<LDFLAGS>']` to inherit the value of the `LDFLAGS` environment variable from your runtime environment target.

Can be overriden by field `python_native_code_ld_flags` on `local_environment`, `docker_environment`, or `remote_environment` targets.
</div>
<br>


## Deprecated options

None


