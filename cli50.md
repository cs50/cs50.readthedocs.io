# `cli50`

`cli50` is a command-line tool via which you can (easily!) mount a directory within a container running [`cs50/cli`](cs50/cli), a Docker image based on Ubuntu 20.04, a popular distribution of Linux. We use `cli50` to work on CS50's own apps in a standard, contained environment, without having to install apps' dependencies on our own Macs and PCs. It provides a command-line environment similar, but not quite identical to, a terminal window on [CS50 IDE](ide/index).

## Installation

1. Install [Docker](/docker), if you haven't already.
1. Install [Python 3.6](/python) or later, if you haven't already.
1. Install [`pip`](/pip), if you haven't already.
1. Install `cli50` itself:
    ```text
    pip3 install cli50
    ```

### Upgrading

```text
pip install --upgrade cli50
```

## Usage

```text
usage: cli50 [-h] [-d DOTFILE] [-f] [-j] [-l [CONTAINER]] [-p PORT] [-S] [-t TAG] [-V] [DIRECTORY]

positional arguments:
  DIRECTORY             directory to mount, else $PWD

optional arguments:
  -h, --help            show this help message and exit
  -d DOTFILE, --dotfile DOTFILE
                        dotfile in your $HOME to mount read-only in container's $HOME
  -f, --fast            don't check for updates
  -j, --jekyll          serve Jekyll site
  -l [CONTAINER], --login [CONTAINER]
                        log into CONTAINER
  -p PORT, --port PORT  publish PORT
  -S, --stop            stop any containers
  -t TAG, --tag TAG     start cs50/cli:TAG, else cs50/cli:latest
  -V, --version         show program's version number and exit
```

## Examples

### Mount current working directory

```text
cli50
```

Your current working directory will be mounted in `/mnt` within the container.

### Mount any directory

Assuming `path/to/directory` is that directory's absolute path, you can mount it within the container as follows:

```text
cli50 path/to/directory
```

The directory will be mounted in `/mnt` within the container.

### Mount dotfile

You can additionally mount a dotfile (or any other file or directory) read-only in `$HOME` within the container as follows:

```text
cli50 ~/.file
```

For instance, it might be useful to mount one's own `.bashrc`:

```text
cli50 -d ~/.bashrc
```

Or one's `.ssh` directory, so that you can use your own SSH keys within the container:

```text
cli50 -d ~/.ssh
```

### Don't check for updates

By default, `cli50` checks for updates to itself as well as `cs50/cli`, the Docker image on which it's based. You can skip those checks as follows:

```text
cli50 -f
```

### Log into running container

If a container (based on any Docker image, [`cs50/cli`](cs50/cli) or otherwise) is already running, you can spawn a login shell within it as follows:

```text
cli50 -l
```

If multiple containers are running, you'll be asked, yes or no, in reverse-chronological order, into which container you'd like to log in.

### Mount `~/.*` in container's `$HOME`

You can mount, read-only, a dotfile that's in your `$HOME` (e.g., `~/.vimrc`) inside of a container's `$HOME` as follows:

```text
cli50 -d .vimrc
```

Directories (e.g., `~/.vim`) are supported as well:

```text
cli50 -d .vim
```

### Exposing a port

By default, `cli50` exposes TCP ports 5000 and 8080, whereby those ports in the container will be mapped to the same on the host (or, if already in use, to pseudorandom ports). You can expose other ports (between 1024 and 65535, inclusive) instead too.

You can expose a single port (e.g., 1024) as follows:

```text
cli50 -p 1024
```

Or you can expose multiple ports (e.g., 1024 and 65535) as follows:

```text
cli50 -p 1024 -p 65535
```

## Source Code

<https://github.com/cs50/cli50>
