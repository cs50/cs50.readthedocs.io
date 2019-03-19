# `cli50`

`cli50` is a command-line tool via which you can (easily!) mount a directory within a container running [`cs50/cli`](cs50/cli), a Docker image based on Ubuntu 18.04, a popular distribution of Linux. We use `cli50` to work on CS50's own apps in a standard, contained environment, without having to install apps' dependencies on our own Macs and PCs. It provides a command-line environment similar, but not quite identical to, a terminal window on [CS50 IDE](/ide). 

## Installation

1. Install [Docker](/docker), if you haven't already.
1. Install [Python 3.6](/python) or later, if you haven't already.
1. Install [`pip`](/pip), if you haven't already.
1. Install `cli50` itself:
    ```
    pip3 install cli50
    ```

### Upgrading

```
pip install --upgrade cli50
```

## Usage

```
usage: cli50 [-h] [-f] [-l [CONTAINER]] [-d DOTFILE] [-S] [-t TAG] [-V]
             [DIRECTORY]

positional arguments:
  DIRECTORY             directory to mount, else $PWD

optional arguments:
  -h, --help            show this help message and exit
  -f, --fast            skip autoupdate
  -l [CONTAINER], --login [CONTAINER]
                        log into container
  -d DOTFILE, --dotfile DOTFILE
                        dotfile in your $HOME to mount read-only in
                        container's $HOME
  -S, --stop            stop any containers
  -t TAG, --tag TAG     start cs50/cli:TAG, else cs50/cli:latest
  -V, --version         show program's version number and exit
```

## Examples

### Mount current working directory

```
cli50
```

Your current working directory will be mounted at `~/workspace` within the container.

### Mount any directory

Assuming `path/to/directory` is that directory's absolute path, you can mount it within the container as follows:

```
cli50 path/to/directory
```

The directory will be mounted at `~/workspace` within the container.

### Skip autoupdate

By default, `cli50` autoupdates (i.e., pulls) `cs50/cli`, the Docker image on which it's based, which can be time-consuming on slow internet connections. You can skip autoupdate as follows:

```
cli50 -f
```

or

```
cli50 --fast
```

### Log into running container

If a container (based on any Docker image, [`cs50/cli`](cs50/cli) or otherwise) is already running, you can spawn a login shell within it as follows:

```
cli50 -l
```

If multiple containers are running, you'll be asked, yes or no, in reverse-chronological order, into which container you'd like to log in.

### Mount `~/.*` in container's `$HOME`

You can mount, read-only, a dotfile that's in your `$HOME` (e.g., `~/.vimrc`) inside of a container's `$HOME` as follows:

```
cli50 -d .vimrc
```

Directories (e.g., `~/.vim`) are supported as well:

```
cli50 -d .vim
```

## Source Code

<https://github.com/cs50/cli50>
