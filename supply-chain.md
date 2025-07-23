I think currently the Pants installation process doesn't give a reliably "verified" environment. Fortunately, I think it's achievable to improve this of the Pants installation process, now that we have far more automated releases (as usual, kudos to @thejcannon). Summary:

1. (optionally) verify hashes for `scie-pants` installation
2. (optionally) verify hashes for `pants` PEX installation
3. lockfiles for pants plugin requirement installation
4. eventually, signing and/or SLSA provenance

In this discussion, I make proposals for seemingly low effort ways to implement 1 and 2, with background/discussion for 3 and 4.

## Background

Once Pants is installed and ready to run, Pants has tools for achieving reasonable supply chain assurance, with lockfiles and hashes on tool downloads (etc.) that can detect some sorts of supply chain attacks. However, there's much less assurance for the Pants installation.

In particular, Pants has a "trust on first use" approach similar to many build tools these: it will detect and fail to build if there's been an attack/change after the first time a lockfile was generated (or when the tool hash was put into `pants.toml`/pants' backends), like a man-in-the-middle attack or reupload of a compromised binary.

(Pants doesn't currently try to verify signatures for `file`/tool downloads, and, AIUI, most language tools like pip don't support them either.)

When installing a pants environment, most of these don't happen. For instance, CI is likely to run something like (https://www.pantsbuild.org/docs/installation):

1. `./get-pants.sh` (hopefully it's checked in!) which downloads the latest release of https://github.com/pantsbuild/scie-pants (or some pinned version) to get the `pants` runner, e.g. https://github.com/pantsbuild/scie-pants/releases/tag/v0.10.4
3. then `pants version` or similar, which:
   1. downloads a Pants PEX, e.g. https://github.com/pantsbuild/pants/releases/tag/release_2.18.0
   2. potentially installs arbitrary Python requirements from PyPI for plugins (e.g. `[GLOBAL].plugins = ["hdrhistogram"]` as recommended in https://www.pantsbuild.org/docs/using-pants-in-ci)

Each of these steps _could_ be compromised in a currently-undetected way:

- for step 1, replace the `scie-pants` binary _and_ the `.sha256` file with a compromised binary
- for step 2a, replace the `pants....pex` PEX with a compromised binary
- for step 2b, publish a new version of a package that matches the requirement constraints to PyPI (NB. this "compromise" is most likely, and could just mean broken builds, if the new version is just different)

## 1. verified `scie-pants` installation

Currently the `scie-pants` releases include `.sha256` hash files, which `get-pants.sh` reads... but they're from the same remote source, and so are untrusted. They're useful for validating that the `scie-pants` binary was downloaded correctly, but not for verifying that it was the intended binary: if someone can modify the binary, they can modify the hash file.

**Proposal**: support a `--hashes` argument to `get-pants.sh`, like:

```
./get-pants.sh --version=v0.10.4 \
   --hash=a2fc54faf40e5b39b7568b35ee21f902665c0081856cad8802ff93f10e811b3b \
   --hash=0873fd861313fd62e4781ee5370be59ad8a1cf6d43868e93ecf421b73a993f7f
```

This argument:

- requires `--version` to be set
- can be specified multiple times (inspired by the pip's similar feature for requirements https://pip.pypa.io/en/stable/topics/secure-installs/#multiple-hashes-per-package)
- is the SHA-256 hash
- the download would be confirmed to match one of the hashes

Thus, one have CI or other scripts hardcode this, and that'd give assurance that only specific `scie-pants` binaries would be installed. The example above would run successfully on Linux x86-64 (`0873fd...`) or Linux AArch64 (`a2fc54...`).

We can make it easy for users to trust-on-first-use by having the automated scie-pants release notes mention the appropriate invocation in the release notes (i.e. something like the above, with all of the hashes).

Alternatives I brainedstormed:

1. require specifying the platform and/or length in addition to hashes, similar to Pants' usual tool download "known versions" syntax, e.g. `"5.1.0|macos_x86_64|c9378d9f4293fc38ec54a08fbc74e7a9d28914dae6891334401e59f38f6e65dc|7125968"`. This doesn't seem necessary for this particular problem.

## 2. verified `pants` PEX installation

Once `scie-pants` is installed, it will go fetch a Pants PEX for the current platform from GitHub releases, without any sort of verification.

**Proposal**: a `[GLOBAL].pants_version_artifact_hashes` setting:
```toml
[GLOBAL]
pants_version = "2.18.0"
pants_version_artifact_hashes = [
     "f14da697f88651f63ace0a192394ed488700c1b2be5a2992f5bf3c7a8041eadb",
     "9d71a5b78ecbd2fd52191666378b31a08cf278a9a8d30eaedb340c61968afd63"
]
```


As above, this is multiple SHA-256 hashes, and `scie-pants` would verify that the downloaded PEX matches one of them.

The examples there would allow installation on macOS (ARM64, x86-64).

The proposal has these in `pants.toml` because `scie-pants` already has to read it (to get `pants_version`). However, it has the downside of Pants itself having Opinions: if one is attempting to use this with an older version of Pants that doesn't know the options exist (or if/when we want to add new options related to this), one will have to set `[GLOBAL].verify_config = false`. I think this is okay... but see the alternatives.

As with `scie-pants` installation, we can make it easy for users to trust-on-first-use by having the automated release notes mention the appropriate configuration in the release notes (i.e. something like the above, with all of the hashes).

Alternatives I brainedstormed:

1. as above, require platform and length in addition to hash
2. instead of a `[GLOBAL]` option, have a `[pants-installation]` section in `pants.toml` that's read by `scie-pants`, which can include a `hashes` key. This could be entirely ignored by Pants itself, making evolution easier

    ```toml
    [GLOBAL]
    pants_version = "2.18.0"

    ...

    [pants-installation]
    hashes = [
         "f14da697f88651f63ace0a192394ed488700c1b2be5a2992f5bf3c7a8041eadb",
         "9d71a5b78ecbd2fd52191666378b31a08cf278a9a8d30eaedb340c61968afd63"
    ]
    ```
3. a separate dedicated file, e.g. `.pants-bootstrap-hashes` or similar.
4. (this could be applied in addition to any solution above) have `scie-pants` itself has some known hashes embedded into it, e.g. all the artifacts for all stable releases, so that someone who happens to be using a `scie-pants` that knows about Pants 2.18.0 would automatically get increased supply chain security (they would then have to switch to manual verification (or upgrade `scie-pants`) if they upgraded to Pants 2.34.0, that wasn't in the `scie-pants` binary).


## 3. Lockfiles for plugin requirements

I've filed a few days ago as https://github.com/pantsbuild/pants/issues/20166 and is what prompted me down this line of thought. I don't have a proposal here, other than something with a PEX lockfile, I guess. Maybe we'd have to package PEX itself into `scie-pants`, or include the PEX tools in the scie-pants PEXes. Do you have ideas?

For now, we have a workaround: a user can achieve increased security by manually pinning all (transitive) dependencies, e.g. `[GLOBAL].plugins = ["hdrhistogram==0.10.3", "pbr==6.0.0"]` instead of `[GLOBAL].plugins = ["hdrhistogram"]`. (I wonder if including `--hash=sha256:...` arguments there works?)

## 4. future state: signing and/or SLSA provenance

(Disclaimer, I'm learning about this space progressively, and am not super familiar with it.)

Verifying hashes ensures that changes/compromises don't happen undetected, once one had decided on a particular environment. But... what happens if the compromise happens earlier? For instance, someone publishes a release manually with compromised artifacts: without some sort of signing, all us users will likely just trust those artifacts. :bang:

AIUI, one way to mitigate some of those threats is to sign builds as coming from particular entities. Thus, if someone trusts those entities, they can verify signatures to determine if the artifact is legitimate. For instance, a build from Pants' CI might be signed with some Pants'-y key, that I personally couldn't get access to, so any build I do on my machine won't be legitimate.

It looks like the https://slsa.dev potentially provides a nice way to do this, with something like https://github.com/slsa-framework/slsa-github-generator allowing signing and https://github.com/slsa-framework/slsa-verifier to verify. Alternatively, I guess we could set up some sort of GPG signing infrastructure like some other projects have.

I don't know enough about this space to make concrete proposals here. Do you have experience? Are there other tools we could consider? Other thoughts?
