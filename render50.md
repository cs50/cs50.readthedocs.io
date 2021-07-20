# `render50`

`render50` is a command-line tool with which you can generate syntax-highlighted PDFs of source code. In years past, CS50 generated PDFs of students' submissions so that teaching fellows (TFs) could annotate the PDFs with typed feedback. These days, CS50 generates PDFs of lectures' source code so that students can annotate them during lectures and so that David has a printout of each lecture's source code in front of him during lectures!

PDFs can be annotated (for free) with:

- [Adobe Reader DC](https://acrobat.adobe.com/us/en/acrobat/pdf-reader.html) on macOS and Windows
- [Evince Document Viewer](https://help.ubuntu.com/community/Evince) on Ubuntu Linux
- [Preview](https://support.apple.com/en-us/HT201740) on macOS

## Installation

1. Install [Python 3.6](/python) or later, if you haven't already.
1. Install [`pip`](/pip), if you haven't already.
1. Install `render50` itself:
    ```
    pip3 install render50
    ```
1. [Install WeasyPrint's dependencies](http://weasyprint.readthedocs.io/en/latest/install.html).

### Upgrading

```
pip install --upgrade render50
```

## Usage

```text
usage: render50 [-h] [-b] [-f] [-i INCLUDE] -o OUTPUT [-P] [-r] [-s SIZE] [-S STYLE] [-x EXCLUDE] [-y] [-V] [INPUT ...]

A command-line tool that renders source code as a PDF.

positional arguments:
  INPUT                 file or URL to render

optional arguments:
  -h, --help            show this help message and exit
  -b, --browser         render as a browser would
  -f, --force           overwrite existing files without prompting
  -i INCLUDE, --include INCLUDE
                        pattern to include
  -o OUTPUT, --output OUTPUT
                        file to output
  -P, --no-path         omit paths in headers
  -r, --recursive       recurse into directories
  -s SIZE, --size SIZE  size of page, per https://developer.mozilla.org/en-US/docs/Web/CSS/@page/size
  -S STYLE, --style STYLE
                        style of syntax highlighting, per https://pygments.org/demo/#try
  -x EXCLUDE, --exclude EXCLUDE
                        pattern to exclude
  -y, --side-by-side    render inputs side by side
  -V, --version         show program's version number and exit
```

## Examples

### Render a single file

To generate a PDF (e.g., `foo.pdf`) from a source file (e.g., `bar.c`), execute:

```
render50 -o foo.pdf bar.c
```

### Render multiple files

To generate a PDF (e.g., `foo.pdf`) from multiple source files (e.g., `bar.c` and `baz.c`), execute:

```
render50 -o foo.pdf bar.c baz.c
```

The source files will be rendered in the order in which they're specified on the command line.

### Include files

To generate a PDF (e.g., `foo.pdf`) from multiple source files, including only those that match some pattern (e.g., `*.c`), execute:

```
render50 -i "*.c" -o foo.pdf *
```

Take care to quote (or escape with `\`) any patterns with wildcards, lest your shell glob the pattern before `render50` can.

### Exclude files

To generate a PDF (e.g., `foo.pdf`) from multiple source files, excluding those that match some pattern (e.g., `*.h`), execute:

```
render50 -x "*.h" -o foo.pdf *
```

As before, take care to quote (or escape with `\`) any patterns with wildcards, lest your shell glob the pattern before `render50` can.

### Render two files side by side

To generate a PDF (e.g., `foo.pdf`) with two source files (e.g., `bar.c` and `baz.c`) side by side, execute:

```
render50 -o foo.pdf -y bar.c baz.c
```

To facilitate discussion thereof, the lefthand file's line numbers will be prefixed with `L` while the righthand file's line numbers will be prefixed with `R`.

### Render files recursively

To recurse into directories, invoke `render50` with `-r`.

### Override syntax highlighting

By default, `render50` uses [Pygments](https://pygments.org/)'s `default` stylesheet to for syntax highlighting but also supports all of the styles demonstrated at <https://pygments.org/demo/#try>. You can specify a style with `-S` as follows:

```
render50 -o foo.pdf -S emacs foo.c
```

#### Disable color

To disable color (e.g., for a black-and-white printer), you can use [Pygments](https://pygments.org/)'s `bw` style as follows:

```
render50 -o foo.pdf -S bw foo.c
```

However, that style might still boldface some keywords. You can further disable boldfacing (and color) as follows:

```
render50 -o foo.pdf --style= foo.c
```

### Rendering URLs

To generate a PDF (e.g., `foo.pdf`) with a source file at a URL (e.g., https://github.com/cs50/render50/blob/master/render50), execute:

```
render50 -o foo.pdf https://github.com/cs50/render50/blob/master/render50
```

Note that URLs on `github.com` are handled specially: URLs of the form `https://github.com/*/*/blob/*` are resolved to `https://github.com/*/*/raw/*` so that the file is downloaded from `raw.githubusercontent.com`. And URLs of the form `https://gist.github.com/*/*` (and `https://gist.github.com/*/*#file-*`) are resolved to `https://gist.github.com/*/*/raw` (and `https://gist.github.com/*/*/raw/*`) so that the file is downloaded from `gist.githubusercontent.com`.

### Overriding page size

By default, `render50` outputs letter-sized (8.5" × 11") pages in landscape orientation. To override that default, invoke `render50` with `--size SIZE`, where `SIZE` is [as prescribed by CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/@page/size). Supported values for `SIZE` thus include:

- `letter landscape`
- `letter portrait`
- `A4 landscape`
- `A4 portrait`

## Source Code

<https://github.com/cs50/render50>
