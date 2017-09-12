---
layout: left
---

# `render50`

`render50` is a command-line tool with which you can generate syntax-highlighted PDFs of source code. In years past, CS50 generated PDFs of students' submissions so that teaching fellows (TFs) could annotate the PDFs with typed feedback. These days, CS50 generates PDFs of lectures' source code so that students can annotate them during lectures. And so that David has a printout of each lecture's source code in front of him during lecture!

PDFs can be annotated (for free) with:

- [Adobe Reader DC](https://acrobat.adobe.com/us/en/acrobat/pdf-reader.html) on macOS and Windows
- [Evince Document Viewer](https://help.ubuntu.com/community/Evince) on Ubuntu Linux
- [Preview](https://support.apple.com/en-us/HT201740) on macOS

## Usage

To generate a PDF (e.g., `foo.pdf`) from a source file (e.g., `bar.c`), execute:

```
render50 foo.pdf bar.c
```

To generate a PDF (e.g., `foo.pdf`) from multiple source files (e.g., `bar.c` and `baz.c`), execute:

```
render50 foo.pdf bar.c baz.c
```

The source files will be rendered in the order in which they're specified on the command line.

To generate a PDF (e.g., `foo.pdf`) from multiple source files, including only those that match some pattern (e.g., `*.c`), execute:

```
render50 --include "*.c" foo.pdf *
```

Take care to quote (or escape with `\`) any patterns with wildcards, lest your shell glob the pattern before `render50` can.

To generate a PDF (e.g., `foo.pdf`) from multiple source files, excluding those that match some pattern (e.g., `*.h`), execute:

```
render50 --exclude "*.h" foo.pdf *
```

As before, take care to quote (or escape with `\`) any patterns with wildcards, lest your shell glob the pattern before `render50` can.

To recurse into directories, invoke `render50` with `--recursive` (or `-r`).

To disable syntax highlighting, invoke `render50` with `--no-color`.

By default, `render50` outputs letter-sized (8.5" × 11") pages in landscape orientation. To override that default, invoke `render50` with `--size SIZE`, where `SIZE` is [as prescribed by CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/@page/size). Supported values for `SIZE` thus include:

- `letter landscape`
- `letter portrait`
- `A4 landscape`
- `A4 portrait`

## Installation

`render50` is already installed for you in [CS50 IDE](https://cs50.io/), so no need to install it yourself; simply use it as directed!

If you'd like to install `render50` on your own Mac or PC, so that you can check your code's style without using CS50 IDE, you'll need a command-line environment:

- If running Linux or the like, you already have one! Open a terminal window in your usual way.
- If running Mac OS, you already have one! Open **Applications > Utilities > Terminal**.
- If running Windows, you'll need to install the [Windows Subsystem for Linux](https://msdn.microsoft.com/commandline/wsl/about), which is only supported on Windows 10. Once installed, [run `bash`](https://blogs.windows.com/buildingapps/2016/03/30/run-bash-on-ubuntu-on-windows/).

To install `render50` within that command-line environment:

1. [Install Python](https://www.python.org/downloads/) 2.7 or higher, if not already installed.

1. Install `pip`, as via 

   ```
   sudo easy_install pip
   ```

   if not already installed.

1. Execute 

   ```
   sudo pip install render50
   ```
   to install `render50` itself.

## Upgrading

Execute

```
sudo pip install --upgrade render50
```

to upgrade `render50`, once installed.

## Implementation Details

To view the source code for `render50`, see <https://github.com/cs50/render50>.
