Configuration of a local execution environment for specific platforms.

Environment configuration includes the platforms the environment is compatible with, and optionally a fallback environment, along with environment-aware options (such as environment variables and search paths) used by Pants to execute processes in this environment.

To use this environment, map this target's address with a memorable name in `[environments-preview].names`. You can then consume this environment by specifying the name in the `environment` field defined on other targets.

Only one `local_environment` may be defined in `[environments-preview].names` per platform, and when `__local__` is specified as the environment, the `local_environment` that matches the current platform (if defined) will be selected.

Backend: <span style="color: purple"><code>pants.core</code></span>

## <code>apache_thrift_thrift_search_paths</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.codegen.thrift.apache.python</code></span>

Overrides the default value from the option `[apache-thrift].thrift_search_paths` when this environment target is active.

## <code>compatible_platforms</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>(&#x27;linux&lowbar;arm64&#x27;, &#x27;linux&lowbar;x86&lowbar;64&#x27;, &#x27;macos&lowbar;arm64&#x27;, &#x27;macos&lowbar;x86&lowbar;64&#x27;)</code></span>

Which platforms this environment can be used with.

This is used for Pants to automatically determine which environment target to use for the user's machine when the environment is set to the special value `__local__`. Currently, there cannot be more than one environment target registered in `[environments-preview].names` for a particular platform. If there is no environment target for a certain platform, Pants will use the options system instead to determine environment variables and executable search paths.

## <code>description</code>

<span style="color: purple">type: <code>str | None</code></span>
<span style="color: green">default: <code>None</code></span>

A human-readable description of the target.

Use `./pants list --documented ::` to see all targets with descriptions.

## <code>docker_env_vars</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.docker, pants.backend.docker.lint.hadolint, pants.backend.experimental.helm</code></span>

Overrides the default value from the option `[docker].env_vars` when this environment target is active.

## <code>docker_executable_search_paths</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.docker, pants.backend.docker.lint.hadolint, pants.backend.experimental.helm</code></span>

Overrides the default value from the option `[docker].executable_search_paths` when this environment target is active.

## <code>fallback_environment</code>

<span style="color: purple">type: <code>str | None</code></span>
<span style="color: green">default: <code>None</code></span>

The environment to fallback to when this local environment cannot be used because the field `compatible_platforms` is not compatible with the local host.

Must be an environment name from the option `[environments-preview].names`, the special string `__local__` to use the relevant local environment, or the Python value `None` to error when this specific local environment cannot be used.

Tip: when targeting Linux, it can be particularly helpful to fallback to a `docker_environment` or `remote_environment` target. That allows you to prefer using the local host when possible, which often has less overhead (particularly compared to Docker). If the local host is not compatible, then Pants will use Docker or remote execution to still run in a similar environment.

## <code>go_generate_env_vars</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.go</code></span>

Overrides the default value from the option `[go-generate].env_vars` when this environment target is active.

## <code>golang_cgo_c_flags</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.go</code></span>

Overrides the default value from the option `[golang].cgo_c_flags` when this environment target is active.

## <code>golang_cgo_cxx_flags</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.go</code></span>

Overrides the default value from the option `[golang].cgo_cxx_flags` when this environment target is active.

## <code>golang_cgo_fortran_binary_name</code>

<span style="color: purple">type: <code>str | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.go</code></span>

Overrides the default value from the option `[golang].cgo_fortran_binary_name` when this environment target is active.

## <code>golang_cgo_fortran_flags</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.go</code></span>

Overrides the default value from the option `[golang].cgo_fortran_flags` when this environment target is active.

## <code>golang_cgo_gcc_binary_name</code>

<span style="color: purple">type: <code>str | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.go</code></span>

Overrides the default value from the option `[golang].cgo_gcc_binary_name` when this environment target is active.

## <code>golang_cgo_gxx_binary_name</code>

<span style="color: purple">type: <code>str | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.go</code></span>

Overrides the default value from the option `[golang].cgo_gxx_binary_name` when this environment target is active.

## <code>golang_cgo_linker_flags</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.go</code></span>

Overrides the default value from the option `[golang].cgo_linker_flags` when this environment target is active.

## <code>golang_cgo_tool_search_paths</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.go</code></span>

Overrides the default value from the option `[golang].cgo_tool_search_paths` when this environment target is active.

## <code>golang_go_search_paths</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.go</code></span>

Overrides the default value from the option `[golang].go_search_paths` when this environment target is active.

## <code>golang_subprocess_env_vars</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.go</code></span>

Overrides the default value from the option `[golang].subprocess_env_vars` when this environment target is active.

## <code>jvm_global_options</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.java, pants.backend.experimental.codegen.protobuf.scala, pants.backend.experimental.java, pants.backend.experimental.java.lint.google_java_format, pants.backend.experimental.kotlin, pants.backend.experimental.kotlin.lint.ktlint, pants.backend.experimental.scala, pants.backend.experimental.scala.lint.scalafmt</code></span>

Overrides the default value from the option `[jvm].global_options` when this environment target is active.

## <code>pex_executable_search_paths</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.awslambda.python, pants.backend.codegen.protobuf.python, pants.backend.docker, pants.backend.docker.lint.hadolint, pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.helm, pants.backend.experimental.python, pants.backend.experimental.python.lint.add_trailing_comma, pants.backend.experimental.python.lint.autoflake, pants.backend.experimental.python.lint.pyupgrade, pants.backend.experimental.terraform, pants.backend.google_cloud_function.python, pants.backend.python, pants.backend.python.lint.bandit, pants.backend.python.lint.black, pants.backend.python.lint.docformatter, pants.backend.python.lint.flake8, pants.backend.python.lint.isort, pants.backend.python.lint.pylint, pants.backend.python.lint.yapf, pants.backend.python.typecheck.mypy, pants.core</code></span>

Overrides the default value from the option `[pex].executable_search_paths` when this environment target is active.

## <code>python_bootstrap_names</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.awslambda.python, pants.backend.codegen.protobuf.python, pants.backend.docker, pants.backend.docker.lint.hadolint, pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.codegen.protobuf.java, pants.backend.experimental.codegen.protobuf.scala, pants.backend.experimental.helm, pants.backend.experimental.java, pants.backend.experimental.java.lint.google_java_format, pants.backend.experimental.kotlin, pants.backend.experimental.kotlin.lint.ktlint, pants.backend.experimental.openapi.lint.spectral, pants.backend.experimental.python, pants.backend.experimental.python.lint.add_trailing_comma, pants.backend.experimental.python.lint.autoflake, pants.backend.experimental.python.lint.pyupgrade, pants.backend.experimental.scala, pants.backend.experimental.scala.lint.scalafmt, pants.backend.experimental.terraform, pants.backend.google_cloud_function.python, pants.backend.python, pants.backend.python.lint.bandit, pants.backend.python.lint.black, pants.backend.python.lint.docformatter, pants.backend.python.lint.flake8, pants.backend.python.lint.isort, pants.backend.python.lint.pylint, pants.backend.python.lint.yapf, pants.backend.python.typecheck.mypy, pants.backend.shell, pants.core</code></span>

Overrides the default value from the option `[python-bootstrap].names` when this environment target is active.

## <code>python_bootstrap_search_path</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.awslambda.python, pants.backend.codegen.protobuf.python, pants.backend.docker, pants.backend.docker.lint.hadolint, pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.codegen.protobuf.java, pants.backend.experimental.codegen.protobuf.scala, pants.backend.experimental.helm, pants.backend.experimental.java, pants.backend.experimental.java.lint.google_java_format, pants.backend.experimental.kotlin, pants.backend.experimental.kotlin.lint.ktlint, pants.backend.experimental.openapi.lint.spectral, pants.backend.experimental.python, pants.backend.experimental.python.lint.add_trailing_comma, pants.backend.experimental.python.lint.autoflake, pants.backend.experimental.python.lint.pyupgrade, pants.backend.experimental.scala, pants.backend.experimental.scala.lint.scalafmt, pants.backend.experimental.terraform, pants.backend.google_cloud_function.python, pants.backend.python, pants.backend.python.lint.bandit, pants.backend.python.lint.black, pants.backend.python.lint.docformatter, pants.backend.python.lint.flake8, pants.backend.python.lint.isort, pants.backend.python.lint.pylint, pants.backend.python.lint.yapf, pants.backend.python.typecheck.mypy, pants.backend.shell, pants.core</code></span>

Overrides the default value from the option `[python-bootstrap].search_path` when this environment target is active.

## <code>python_native_code_cpp_flags</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.awslambda.python, pants.backend.codegen.protobuf.python, pants.backend.docker, pants.backend.docker.lint.hadolint, pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.helm, pants.backend.experimental.python, pants.backend.experimental.python.lint.add_trailing_comma, pants.backend.experimental.python.lint.autoflake, pants.backend.experimental.python.lint.pyupgrade, pants.backend.experimental.terraform, pants.backend.google_cloud_function.python, pants.backend.python, pants.backend.python.lint.bandit, pants.backend.python.lint.black, pants.backend.python.lint.docformatter, pants.backend.python.lint.flake8, pants.backend.python.lint.isort, pants.backend.python.lint.pylint, pants.backend.python.lint.yapf, pants.backend.python.typecheck.mypy, pants.core</code></span>

Overrides the default value from the option `[python-native-code].cpp_flags` when this environment target is active.

## <code>python_native_code_ld_flags</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.awslambda.python, pants.backend.codegen.protobuf.python, pants.backend.docker, pants.backend.docker.lint.hadolint, pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.helm, pants.backend.experimental.python, pants.backend.experimental.python.lint.add_trailing_comma, pants.backend.experimental.python.lint.autoflake, pants.backend.experimental.python.lint.pyupgrade, pants.backend.experimental.terraform, pants.backend.google_cloud_function.python, pants.backend.python, pants.backend.python.lint.bandit, pants.backend.python.lint.black, pants.backend.python.lint.docformatter, pants.backend.python.lint.flake8, pants.backend.python.lint.isort, pants.backend.python.lint.pylint, pants.backend.python.lint.yapf, pants.backend.python.typecheck.mypy, pants.core</code></span>

Overrides the default value from the option `[python-native-code].ld_flags` when this environment target is active.

## <code>shell_setup_executable_search_path</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.shell</code></span>

Overrides the default value from the option `[shell-setup].executable_search_path` when this environment target is active.

## <code>subprocess_environment_env_vars</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.awslambda.python, pants.backend.codegen.protobuf.python, pants.backend.docker, pants.backend.docker.lint.hadolint, pants.backend.experimental.codegen.protobuf.go, pants.backend.experimental.helm, pants.backend.experimental.python, pants.backend.experimental.python.lint.add_trailing_comma, pants.backend.experimental.python.lint.autoflake, pants.backend.experimental.python.lint.pyupgrade, pants.backend.experimental.terraform, pants.backend.google_cloud_function.python, pants.backend.python, pants.backend.python.lint.bandit, pants.backend.python.lint.black, pants.backend.python.lint.docformatter, pants.backend.python.lint.flake8, pants.backend.python.lint.isort, pants.backend.python.lint.pylint, pants.backend.python.lint.yapf, pants.backend.python.typecheck.mypy, pants.core</code></span>

Overrides the default value from the option `[subprocess-environment].env_vars` when this environment target is active.

## <code>tags</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>

Arbitrary strings to describe a target.

For example, you may tag some test targets with 'integration_test' so that you could run `./pants --tag='integration_test' test ::` to only run on targets with that tag.

## <code>test_extra_env_vars</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>
backend: <span style="color: green"><code>pants.backend.experimental.codegen.protobuf.java, pants.backend.experimental.go, pants.backend.experimental.helm, pants.backend.experimental.java, pants.backend.experimental.kotlin, pants.backend.experimental.kotlin.lint.ktlint, pants.backend.experimental.scala, pants.backend.experimental.scala.lint.scalafmt, pants.backend.python, pants.backend.shell, pants.core</code></span>

Overrides the default value from the option `[test].extra_env_vars` when this environment target is active.

