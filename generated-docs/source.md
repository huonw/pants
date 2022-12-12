
Configuration for roots of source trees.

Backend: <span style="color: purple"><code>pants.backend.awslambda.python, pants.backend.codegen.protobuf.python, pants.backend.codegen.thrift.apache.python, pants.backend.experimental.codegen.protobuf.java, pants.backend.experimental.codegen.protobuf.scala, pants.backend.experimental.java, pants.backend.experimental.kotlin, pants.backend.experimental.kotlin.lint.ktlint, pants.backend.experimental.python, pants.backend.experimental.scala, pants.backend.experimental.scala.lint.scalafmt, pants.backend.google_cloud_function.python, pants.backend.python, pants.backend.python.lint.flake8, pants.backend.python.lint.pylint, pants.backend.python.typecheck.mypy, pants.core</code></span>
Config section: <span style="color: purple"><code>[source]</code></span>

## Basic options

None

## Advanced options

<div style="color: purple">

### `root_patterns`

  <code>--source-root-patterns=&quot;[[&quot;pattern1&quot;, &quot;pattern2&quot;, ...], [&quot;pattern1&quot;, &quot;pattern2&quot;, ...], ...]&quot;</code><br>
  <code>PANTS_SOURCE_ROOT_PATTERNS</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <pre>[
  "/",
  "src",
  "src/python",
  "src/py",
  "src/thrift",
  "src/protobuf",
  "src/protos",
  "src/scala",
  "src/java"
]</pre></span>

<br>

A list of source root suffixes. A directory with this suffix will be considered a potential source root. E.g., `src/python` will match `<buildroot>/src/python`, `<buildroot>/project1/src/python` etc. Prepend a `/` to anchor the match at the buildroot. E.g., `/src/python` will match `<buildroot>/src/python` but not `<buildroot>/project1/src/python`. A `*` wildcard will match a single path segment, e.g., `src/*` will match `<buildroot>/src/python` and `<buildroot>/src/rust`. Use `/` to signify that the buildroot itself is a source root. See https://www.pantsbuild.org/v2.16/docs/source-roots.
</div>
<br>

<div style="color: purple">

### `marker_filenames`

  <code>--source-marker-filenames=&quot;[filename, filename, ...]&quot;</code><br>
  <code>PANTS_SOURCE_MARKER_FILENAMES</code><br>
</div>
<div style="padding-left: 2em;">
<span style="color: green">default: <code>[]</code></span>

<br>

The presence of a file of this name in a directory indicates that the directory is a source root. The content of the file doesn't matter, and may be empty. Useful when you can't or don't wish to centrally enumerate source roots via `root_patterns`.
</div>
<br>


## Deprecated options

None


