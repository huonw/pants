```
./pants python-dump-source-analysis [args]
```
Dump source analysis for python_source targets.

Backend: <span style="color: purple"><code>pants.backend.experimental.python</code></span>
Config section: <span style="color: purple"><code>[python-dump-source-analysis]</code></span>

## Basic options

<div style="color: purple">

### `analysis_flavor`

  <code>--python-dump-source-analysis-analysis-flavor=&lt;AnalysisFlavor&gt;</code><br>
  <code>PANTS_PYTHON_DUMP_SOURCE_ANALYSIS_ANALYSIS_FLAVOR</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">one of: <code>raw_dependency_inference, dependency_inference</code></span><br>
<span style="color: green">default: <code>dependency&lowbar;inference</code></span>

<br>

The type of information that should be returned.

* `dependency_inference`: The results of dependency inference, for every detected import in every file.

* `raw_dependency_inference`: The raw intermediate results of the dependency inference process,
at every stage they're available. Potentially useful for debugging the dependency inference process.
</div>
<br>


## Advanced options

None

## Deprecated options

None


## Related subsystems
[environments-preview](environments-preview.md), [filter](filter.md), [pex](pex.md), [pex-cli](pex-cli.md), [python](python.md), [python-bootstrap](python-bootstrap.md), [python-infer](python-infer.md), [python-native-code](python-native-code.md), [source](source.md), [subprocess-environment](subprocess-environment.md)
