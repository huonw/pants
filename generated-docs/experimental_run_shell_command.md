Run a script in the workspace, with all dependencies packaged/copied into a chroot.

Example BUILD file:

    experimental_run_shell_command(
        command="./scripts/my-script.sh --data-files-dir={chroot}",
        execution_dependencies=["src/project/files:data"],
    )

The `command` may use either `{chroot}` on the command line, or the `$CHROOT` environment variable to get the root directory for where any dependencies are located.

In contrast to the `experimental_shell_command`, in addition to `workdir` you only have the `command` and `execution_dependencies` fields as the `tools` you are going to use are already on the PATH which is inherited from the Pants environment. Also, the `outputs` does not apply, as any output files produced will end up directly in your project tree.

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

## <code>execution_dependencies</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>

The execution dependencies for this shell command.

Dependencies specified here are those required to make the command complete successfully (e.g. file inputs, binaries compiled from other targets, etc), but NOT required to make the output side-effects useful. Dependencies that are required to use the side-effects produced by this command should be specified using the `output_dependencies` field.

If this field is specified, dependencies from `output_dependencies` will not be added to the execution sandbox.

## <code>tags</code>

<span style="color: purple">type: <code>Iterable[str] | None</code></span>
<span style="color: green">default: <code>None</code></span>

Arbitrary strings to describe a target.

For example, you may tag some test targets with 'integration_test' so that you could run `./pants --tag='integration_test' test ::` to only run on targets with that tag.

## <code>workdir</code>

<span style="color: purple">type: <code>str | None</code></span>
<span style="color: green">default: <code>&#x27;.&#x27;</code></span>

Sets the current working directory of the command, relative to the project root.

