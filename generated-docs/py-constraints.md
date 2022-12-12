```
./pants py-constraints [args]
```
Determine what Python interpreter constraints are used by files/targets.

Backend: <span style="color: purple"><code>pants.backend.python.mixed_interpreter_constraints</code></span>
Config section: <span style="color: purple"><code>[py-constraints]</code></span>

## Basic options

<div style="color: purple">

### `output_file`

  <code>--py-constraints-output-file=&lt;path&gt;</code><br>
  <code>PANTS_PY_CONSTRAINTS_OUTPUT_FILE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>None</code></span>

<br>

Output the goal's stdout to this file. If unspecified, outputs to stdout.
</div>
<br>

<div style="color: purple">

### `summary`

  <code>--[no-]py-constraints-summary</code><br>
  <code>PANTS_PY_CONSTRAINTS_SUMMARY</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

Output a CSV summary of interpreter constraints for your whole repository. The headers are `Target`, `Constraints`, `Transitive Constraints`, `# Dependencies`, and `# Dependents` (or `# Dependees`, if summary_use_new_header is False).

This information can be useful when prioritizing a migration from one Python version to another (e.g. to Python 3). Use `# Dependencies` and `# Dependents` to help prioritize which targets are easiest to port (low # dependencies) and highest impact to port (high # dependents).

Use a tool like Pandas or Excel to process the CSV. Use the option `--py-constraints-output-file=summary.csv` to write directly to a file.
</div>
<br>

<div style="color: purple">

### `summary_use_new_header`

  <code>--[no-]py-constraints-summary-use-new-header</code><br>
  <code>PANTS_PY_CONSTRAINTS_SUMMARY_USE_NEW_HEADER</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

If False, use the legacy, misleading `#Dependees` header name in the summary CSV table. If True, will use the new, more accurate, `# Dependents` name for the same column.

This is a temporary option to ease migration to the new header name. Set this option to True to start working with the new header.

This option's default value will change to True in 2.16.x, and it will be deprecated in that version.

This option, and the ability to use the old name, will be removed entirely in 2.17.x.
</div>
<br>


## Advanced options

None

## Deprecated options

None


## Related subsystems
[environments-preview](environments-preview.md), [filter](filter.md), [python](python.md)
