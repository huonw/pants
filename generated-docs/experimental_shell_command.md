Execute any external tool for its side effects.

Example BUILD file:

    experimental_shell_command(
        command="./my-script.sh --flag",
        tools=["tar", "curl", "cat", "bash", "env"],
        execution_dependencies=[":scripts"],
        output_files=["logs/my-script.log"],
        output_directories=["results"],
    )

    shell_sources(name="scripts")

Remember to add this target to the dependencies of each consumer, such as your `python_tests` or `docker_image`. When relevant, Pants will run your `command` and insert the `outputs` into that consumer's context.

The command may be retried and/or cancelled, so ensure that it is idempotent.

Backend: <span style="color: purple"><code>pants.backend.shell</code></span>

## <code>command</code>

<span style="color: purple">type: <code>str</code></span>
<span style="color: green">required</span>

Shell command to execute.

The command is executed as 'bash -c <command>' by default.

## <code>description</code>

<span style="color: purple">type: <code>str | None</code></span>
<span style="color: green">default: <code>None</code></span>

A human-readable description of the target.

Use `./pants list --documented ::` to see all targets with descriptions.

## <code>environment</code>

<span style="color: purple">type: <code>str | None</code></span>
<span style="color: green">default: <code>&#x27;&lowbar;&lowbar;local&lowbar;&lowbar;&#x27;</code></span>

Specify which environment target to consume environment-sensitive options from.

Once environments are defined in `[environments-preview].names`, you can specify the environment for this target by its name. Any fields that are defined in that environment will override the values from options set by `pants.toml`, command line values, or environment variables.

You can specify multiple valid environments by using `parametrize`. If `__local__` is specified, Pants will fall back to the `local_environment` defined for the current platform, or no environment if no such environment exists.

## <code>execution_dependencies</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>

The execution dependencies for this shell command.

Dependencies specified here are those required to make the command complete successfully (e.g. file inputs, binaries compiled from other targets, etc), but NOT required to make the output side-effects useful. Dependencies that are required to use the side-effects produced by this command should be specified using the `output_dependencies` field.

If this field is specified, dependencies from `output_dependencies` will not be added to the execution sandbox.

## <code>extra_env_vars</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>

Additional environment variables to include in the shell process. Entries are strings in the form `ENV_VAR=value` to use explicitly; or just `ENV_VAR` to copy the value of a variable in Pants's own environment.

## <code>log_output</code>

<span style="color: purple">type: <code>bool</code></span>
<span style="color: green">default: <code>False</code></span>

Set to true if you want the output from the command logged to the console.

## <code>output_dependencies</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>

Any dependencies that the output artifacts require in order to be effectively consumed.

To enable legacy use cases, if `execution_dependencies` is `None`, these dependencies will be materialized in the command execution sandbox. This behavior is deprecated, and will be removed in version 2.17.0.dev0.

## <code>output_directories</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>()</code></span>

Specify full directories (including recursive descendants) of output to capture from the shell command.

For files, use `output_files`. At least one of `output_files` and `output_directories` must be specified.

## <code>output_files</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>()</code></span>

Specify the shell command's output files to capture.

For directories, use `output_directories`. At least one of `output_files` and `output_directories` must be specified.

## <code>tags</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>

Arbitrary strings to describe a target.

For example, you may tag some test targets with 'integration_test' so that you could run `./pants --tag='integration_test' test ::` to only run on targets with that tag.

## <code>timeout</code>

<span style="color: purple">type: <code>int | None</code></span>
<span style="color: green">default: <code>30</code></span>

Command execution timeout (in seconds).

## <code>tools</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>()</code></span>

Specify required executable tools that might be used.

Only the tools explicitly provided will be available on the search PATH, and these tools must be found on the paths provided by [shell-setup].executable_search_paths (which defaults to the system PATH).

