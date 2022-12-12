```
./pants export [args]
```
Export Pants data for use in other tools, such as IDEs.

Backend: <span style="color: purple"><code>pants.core</code></span>
Config section: <span style="color: purple"><code>[export]</code></span>

## Basic options

<div style="color: purple">

### `resolve`

  <code>--export-resolve=&quot;['&lt;str&gt;', '&lt;str&gt;', ...]&quot;</code><br>
  <code>PANTS_EXPORT_RESOLVE</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

Export the specified resolve(s). The export format is backend-specific, e.g., Python resolves are exported as virtualenvs.
</div>
<br>

<div style="color: purple">

### `symlink_python_virtualenv`

  <code>--[no-]export-symlink-python-virtualenv</code><br>
  <code>PANTS_EXPORT_SYMLINK_PYTHON_VIRTUALENV</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>False</code></span>

<br>

Export a symlink into a cached Python virtualenv.  This virtualenv will have no pip binary, and will be immutable. Any attempt to modify it will corrupt the cache!  It may, however, take significantly less time to export than a standalone, mutable virtualenv will.
</div>
<br>


## Advanced options

None

## Deprecated options

None


## Related subsystems
[environments-preview](environments-preview.md), [filter](filter.md)
