---
layout: top
---

# CS50 CLI

CS50 CLI is a [Docker](https://github.com/cs50/cli/blob/master/Dockerfile) image with which you can (easily!) mount a directory within a container running [Ubuntu 14.04](https://hub.docker.com/_/ubuntu/). We use it to work on CS50's own apps in a standard, contained environment, without having to install apps' dependencies on our own Macs and PCs. It provides a command-line environment similar, but not identical to, a terminal window on [CS50 IDE](https://cs50.io/); see [Notes](#notes) for differences.

`cli50` is a command-line script that facilitates using CS50 CLI (so that you needn't type long command lines in order to start a container).

Once [CS50 IDE](https://cs50.io/) migrates from Ubuntu 14.04 LTS to Ubuntu 16.04 will CS50 CLI be migrated as well.

## Installation

Assuming you already have [Docker Engine](https://docs.docker.com/engine/installation/), `python`, and `pip` installed, you can install `cli50` (on Linux, Mac OS, and Windows) with:

```
pip install cli50
```

Or perhaps:

```
sudo pip install cli50
```

## Usage

You can mount your current working directory within CS50 CLI as follows.

```
cli50
```

You can mount some other directory within CS50 CLI as follows, where `path/to/directory` is that directory's absolute path.

```
cli50 path/to/directory
```

If invoked with `--fast` (or `-f`), `cli50` will start CS50 CLI without autoupdating its `cs50/cli` image.

If invoked with `--git` (or `-g`), `cli50` will mount `~/.gitconfig` read-only inside of CS50 CLI.

If invoked with `--ssh` (or `-s`), `cli50` will mount `~/.ssh` read-only inside of CS50 CLI.

## Notes

CS50 CLI differs from a terminal window in [CS50 IDE](https://cs50.io/) in, at least, the following ways

| | CS50 CLI | CS50 IDE
| --- | --- | ---
| Clang | 3.8 | 3.6
| PHP | 7.1 | 5.5
|===

CS50 IDE will eventually be updated to bring it in parity.
