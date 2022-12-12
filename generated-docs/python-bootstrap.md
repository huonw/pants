
Options used to locate Python interpreters used by all Pants backends.

This subsystem controls where and how Pants will locate Python, but beyond that it does not control which Python interpreter versions are actually used for your code: see the `python` subsystem for that.

Backend: <span style="color: purple"><code>pants.core</code></span>
Config section: <span style="color: purple"><code>[python-bootstrap]</code></span>

## Basic options

None

## Advanced options

<div style="color: purple">

### `search_path`

  <code>--python-bootstrap-search-path=&quot;[&lt;binary-paths&gt;, &lt;binary-paths&gt;, ...]&quot;</code><br>
  <code>PANTS_PYTHON_BOOTSTRAP_SEARCH_PATH</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "&lt;PYENV&gt;",
  "&lt;PATH&gt;"
]</pre></span>

<br>

A list of paths to search for Python interpreters.

Which interpeters are actually used from these paths is context-specific: the Python backend selects interpreters using options on the `python` subsystem, in particular, the `[python].interpreter_constraints` option.

You can specify absolute paths to interpreter binaries and/or to directories containing interpreter binaries. The order of entries does not matter.

The following special strings are supported:

For all runtime environment types:

* `<PATH>`, the contents of the PATH env var

When the environment is a `local_environment` target:

* `<ASDF>`, all Python versions currently configured by ASDF `(asdf shell, ${HOME}/.tool-versions)`, with a fallback to all installed versions
* `<ASDF_LOCAL>`, the ASDF interpreter with the version in BUILD_ROOT/.tool-versions
* `<PYENV>`, all Python versions under $(pyenv root)/versions
* `<PYENV_LOCAL>`, the Pyenv interpreter with the version in BUILD_ROOT/.python-version
* `<PEXRC>`, paths in the PEX_PYTHON_PATH variable in /etc/pexrc or ~/.pexrc

Can be overriden by field `python_bootstrap_search_path` on `local_environment`, `docker_environment`, or `remote_environment` targets.
</div>
<br>

<div style="color: purple">

### `names`

  <code>--python-bootstrap-names=&quot;[&lt;python-binary-names&gt;, &lt;python-binary-names&gt;, ...]&quot;</code><br>
  <code>PANTS_PYTHON_BOOTSTRAP_NAMES</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "python",
  "python3"
]</pre></span>

<br>

The names of Python binaries to search for. See the `--search-path` option to influence where interpreters are searched for.

This does not impact which Python interpreter is used to run your code, only what is used to run internal tools.

Can be overriden by field `python_bootstrap_names` on `local_environment`, `docker_environment`, or `remote_environment` targets.
</div>
<br>


## Deprecated options

None


