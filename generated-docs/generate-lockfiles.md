```
./pants generate-lockfiles [args]
```
Generate lockfiles for third-party dependencies.

Backend: <span style="color: purple"><code>pants.backend.awslambda.python, pants.backend.build_files.fmt.black, pants.backend.build_files.fmt.yapf, pants.backend.codegen.protobuf.python, pants.backend.docker, pants.backend.docker.lint.hadolint, pants.backend.experimental.helm, pants.backend.experimental.python, pants.backend.experimental.python.lint.add_trailing_comma, pants.backend.experimental.python.lint.autoflake, pants.backend.experimental.python.lint.pyupgrade, pants.backend.experimental.python.packaging.pyoxidizer, pants.backend.experimental.terraform, pants.backend.google_cloud_function.python, pants.backend.python, pants.backend.python.lint.bandit, pants.backend.python.lint.black, pants.backend.python.lint.docformatter, pants.backend.python.lint.flake8, pants.backend.python.lint.isort, pants.backend.python.lint.pylint, pants.backend.python.lint.yapf, pants.backend.python.typecheck.mypy, pants.core</code></span>
Config section: <span style="color: purple"><code>[generate-lockfiles]</code></span>

## Basic options

<div style="color: purple">

### `resolve`

  <code>--generate-lockfiles-resolve=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_GENERATE_LOCKFILES_RESOLVE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Only generate lockfiles for the specified resolve(s).

Resolves are the logical names for the different lockfiles used in your project. For your own code's dependencies, these come from backend-specific configuration such as `[python].resolves`. For tool lockfiles, resolve names are the options scope for that tool such as `black`, `pytest`, and `mypy-protobuf`.

For example, you can run `./pants generate-lockfiles --resolve=black --resolve=pytest --resolve=data-science` to only generate lockfiles for those two tools and your resolve named `data-science`.

If you specify an invalid resolve name, like 'fake', Pants will output all possible values.

If not specified, Pants will generate lockfiles for all resolves.
</div>
<br>


## Advanced options

<div style="color: purple">

### `custom_command`

  <code>--generate-lockfiles-custom-command=&lt;str&gt;</code><br>
  <code>PANTS_GENERATE_LOCKFILES_CUSTOM_COMMAND</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

If set, lockfile headers will say to run this command to regenerate the lockfile, rather than running `./pants generate-lockfiles --resolve=<name>` like normal.
</div>
<br>


## Deprecated options

None


## Related subsystems
[environments-preview](environments-preview.md)
