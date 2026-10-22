# `style50`

`style50` is a command-line tool with which you can check your code for consistency with CS50's style guides, including [CS50's style guide for C](../style/c/) and [PEP 8](https://peps.python.org/pep-0008/) for Python. It supports C, C++, Java, Python, JavaScript, HTML, CSS, and SQL. If your code isn't styled consistently, `style50` will summarize the changes you should make to your code, as by highlighting in <span class="bg-green p-1 text-white">green</span> characters you should add and highlighting in <span class="bg-red p-1 text-white">red</span> characters you should delete. If fewer than 10% of your code's lines are comments, `style50` will also remind you to add more.

For instance, consider the code below, wherein the call to `printf` isn't properly indented.

```text
#include <stdio.h>

int main(void)
{
printf("hello, world\n");
}
```

Given that code as input, `style50` will output

<div class="highlight-none notranslate"><div class="highlight"><pre>#include &lt;stdio.h&gt;
<br>int main(void)
{
<span style="background-color: #00cc00">    </span>printf("hello, world\n");
}</pre></div></div>

wherein highlighted are four spaces that should be added for style's sake.

On the other hand, consider the code below, wherein the curly braces are unnecessarily indented.

```text
#include <stdio.h>

int main(void)
    {
    printf("hello, world\n");
    }
```

Given that code as input, `style50` will output

<div class="highlight-none notranslate"><div class="highlight"><pre>#include &lt;stdio.h&gt;
<br>int main(void)
<span style="background-color: red">    </span>{
    printf("hello, world\n");
<span style="background-color: red">    </span>}</pre></div></div>

wherein highlighted are four spaces that should be deleted for style's sake.

## Installation

`style50` is already installed for you in [Visual Studio Code for CS50](https://cs50.dev/), so no need to install it yourself; simply use it as directed!

If you'd like to install `style50` on your own Mac or PC, install [Python 3.8](/python) or later, if you haven't already. `style50` also requires `libmagic`, via which it detects file types. If running Linux, install it via your package manager (e.g., `sudo apt install libmagic-dev` on Ubuntu). If running macOS, install it via [Homebrew](https://brew.sh/) with `brew install libmagic`.

### Using `pip`
1. Install [`pip`](/pip), if you haven't already.
2. Install `style50` itself:
    ```text
    pip3 install style50
    ```

### Using `pipx`
1. Install [`pipx`](/pipx), if you haven't already.
2. Install `style50` itself:
    ```text
    pipx install style50
    ```

Note: If on Windows, please first install [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10). We recommend choosing the `Ubuntu` distribution. Then within WSL, follow the above steps to install [Python](/python) and `style50`.

### Upgrading

If using `pip`, you can upgrade `style50` with
```text
pip3 install --upgrade style50
```

If using `pipx`, you can upgrade `style50` with
```text
pipx upgrade style50
```

## Usage

```text
usage: style50 [-h] [-o MODE] [-y] [-i] [-v] [-V] [-E] [--ignore PATTERN]
               [--clang-format-style STYLE]
               FILE [FILE ...]

positional arguments:
  FILE                  file or directory to lint

options:
  -h, --help            show this help message and exit
  -o, --output MODE     output mode, which can be character (default), split,
                        unified, score, json, html, or format
  -y, --side-by-side    show side-by-side diff (equivalent to -o split)
  -i, --in-place        rewrite files in place with style50 formatting
  -v, --verbose         print full tracebacks of errors
  -V, --version         show program's version number and exit
  -E, --extensions      print supported file extensions (as JSON list) and
                        exit
  --ignore PATTERN      paths/patterns to be ignored
  --clang-format-style STYLE
                        clang-format style string or file:// URI (overrides
                        default CS50 config)
```

## Examples

### Checking a file

To check your code's style, execute

```text
style50 file
```

where `file` is the (path to some) file whose style you'd like to check, as with

```text
style50 hello.c
```

### Checking multiple files

You can also check more than one file at once, as with

```text
style50 hello.c hello.py
```

or even an entire directory, as with

```text
style50 .
```

in which case `style50` will check every supported file therein, recursively. To skip some files, use `--ignore`, as with

```text
style50 --ignore "*.html" .
```

### Modes

By default, `style50` operates in [`character`](#character) mode, but you can specify other modes with `-o` or `--output`.

Consider the (poorly styled) file below, `hello.c`, for a look at these modes.

```text
#include <stdio.h>

int main(void)
    {
printf("hello, world\n");
    }
```

#### `character`

In `character` mode, `style50` compares its input against CS50's style guide character by character. Were you to run

```text
style50 --output character hello.c
```

or just

```text
style50 -o character hello.c
```

or even just

```text
style50 hello.c
```

you would see the below.

<div class="highlight-none notranslate"><div class="highlight"><pre>#include &lt;stdio.h&gt;
<br>int main(void)
<span style="background-color: #00cc00">{\n</span>
    <span style="background-color: red">{\n</span>
<span style="background-color: #00cc00">    </span>printf("hello, world\n");
<span style="background-color: red">    </span>}</pre></div></div>

#### `split`

In `split` mode, `style50` displays its input and output side by side. Were you to run

```text
style50 --output split hello.c
```

or just

```text
style50 -y hello.c
```

you would see the below.

<div class="highlight-none notranslate"><div class="highlight"><pre>#include &lt;stdio.h&gt;               #include &lt;stdio.h&gt;
<br>int main(void)                   int main(void)
    <span style="color: red">{</span>                            <span style="color: #00cc00">{</span>
printf("hello, world\n");        <span style="background-color: #00cc00">    </span>printf("hello, world\n");
    <span style="color: red">}</span>                            <span style="color: #00cc00">}</span></pre></div></div>

#### `unified`

In `unified` mode, `style50` displays its output line by line, akin to [`git-diff`](https://git-scm.com/docs/git-diff). Were you to run

```text
style50 --output unified hello.c
```

or just

```text
style50 -o unified hello.c
```

you would see the below.

<div class="highlight-none notranslate"><div class="highlight"><pre>  #include &lt;stdio.h&gt;
<br>  int main(void)
<span style="color: red">-     {</span>
<span style="color: #00cc00">+ {</span>
<span style="color: red">- printf("hello, world\n");</span>
<span style="color: #00cc00">+     printf("hello, world\n");</span>
<span style="color: red">-     }</span>
<span style="color: #00cc00">+ }</span></pre></div></div>

#### `score`

In `score` mode, `style50` outputs only the fraction of lines that are already styled correctly, from `0.0` to `1.0`. Were you to run

```text
style50 -o score hello.c
```

you would see the below.

```text
0.4
```

#### `json`

In `json` mode, `style50` outputs its results as a [JSON](https://en.wikipedia.org/wiki/JSON) object, which is useful if you'd like to use `style50` in a program of your own. Were you to run

```text
style50 -o json hello.c
```

you would see the below.

```text
{
    "files": [
        {
            "name": "hello.c",
            "score": 0.4,
            "comments": true,
            "diff": "<pre>\n#include &lt;stdio.h&gt;\n\nint main(void)\n<ins>{\\n</ins>\n<ins></ins>    <del>{\\n</del><del></del>printf(&quot;hello, world\\n&quot;);\n<del>    </del>}\n</pre>",
            "warn_chars": [
                [
                    "+",
                    "\\n"
                ],
                [
                    "-",
                    "\\n"
                ]
            ],
            "loc": 5
        }
    ],
    "score": 0.4,
    "version": "3.0.0"
}
```

#### `html`

In `html` mode, `style50` saves its results as an HTML file that you can open in a browser. Were you to run

```text
style50 -o html hello.c
```

you would see something like the below.

```text
To see results in your browser go to file:///tmp/tmp0nvr8ghd.html
```

#### `format`

In `format` mode, `style50` outputs only the correctly styled version of a single file, without any highlighting. Were you to run

```text
style50 -o format hello.c
```

you would see the below.

```text
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

### Fixing style automatically

If you'd like `style50` to restyle your code for you, rather than just show you what to change, execute

```text
style50 -i hello.c
```

in which case `style50` will rewrite `hello.c` in place. Note that `-i` can't be combined with `-o` or `-y`.

### Customizing style for C, C++, and Java

Underneath the hood, `style50` uses [`clang-format`](https://clang.llvm.org/docs/ClangFormat.html) to style C, C++, and Java, with the configuration below.

```text
AllowShortFunctionsOnASingleLine: Empty
BraceWrapping:
  AfterCaseLabel: true
  AfterControlStatement: true
  AfterFunction: true
  AfterStruct: true
  BeforeElse: true
  BeforeWhile: true
BreakBeforeBraces: Custom
ColumnLimit: 100
IndentCaseLabels: true
IndentWidth: 4
SpaceAfterCStyleCast: true
TabWidth: 4
```

If you're using `style50` outside of CS50, you can override that configuration with `--clang-format-style`, passing it either a style string, as with

```text
style50 --clang-format-style "{IndentWidth: 2}" hello.c
```

or the path to a [`.clang-format`](https://clang.llvm.org/docs/ClangFormatStyleOptions.html) file, as with

```text
style50 --clang-format-style file://$PWD/.clang-format hello.c
```

Some [options](https://clang.llvm.org/docs/ClangFormatStyleOptions.html) you might want to change:

* `ColumnLimit`, the maximum length of a line, which CS50 sets to `100`.
* `IndentWidth`, the number of spaces per level of indentation, which CS50 sets to `4`.
* `BreakBeforeBraces`, which CS50 sets to `Custom` (with the `BraceWrapping` options above) so that curly braces are on their own lines. Set it to `Attach` instead if you'd prefer curly braces on the same line as, e.g., `int main(void)`.
* `AllowShortFunctionsOnASingleLine`, which CS50 sets to `Empty` so that only empty functions can be on a single line.

In [Visual Studio Code for CS50](https://cs50.dev/), `style50` will automatically use a `.clang-format` file if one exists in your code's directory (or any directory above it), so no need to pass `--clang-format-style` yourself.

## Visual Studio Code for CS50

In [Visual Studio Code for CS50](https://cs50.dev/), `style50` is also built into VS Code itself. Whenever you open a supported file, you'll see a **style50** button in the top-right corner of the editor. Clicking it opens a side-by-side view of your code and the correctly styled version thereof, highlighting the differences, along with two buttons:

* **Apply Changes**, which restyles your code for you.
* **Explain Changes**, which asks the [CS50 Duck](/cs50.ai) to explain the changes.

Alternatively, you can fix your code's style yourself, in which case the side-by-side view will close once your code matches.

Running `style50 hello.c` in a codespace's terminal opens that same side-by-side view, for a single file at a time. If you'd prefer the command-line behavior described above, as for checking multiple files or using other modes, run `style50-cli` instead, as with

```text
style50-cli -o unified hello.c
```

## Languages

`style50` currently supports these languages:

| Language   | Extensions                   | Styled with                                                                   |
|------------|------------------------------|-------------------------------------------------------------------------------|
| C          | `.c`, `.h`                   | [`clang-format`](https://clang.llvm.org/docs/ClangFormat.html)                |
| C++        | `.cpp`, `.hpp`               | [`clang-format`](https://clang.llvm.org/docs/ClangFormat.html)                |
| CSS        | `.css`                       | [`cssbeautifier`](https://pypi.org/project/cssbeautifier/)                    |
| HTML       | `.html`                      | [`djhtml`](https://pypi.org/project/djhtml/)                                  |
| Java       | `.java`                      | [`clang-format`](https://clang.llvm.org/docs/ClangFormat.html)                |
| JavaScript | `.js`                        | [`jsbeautifier`](https://pypi.org/project/jsbeautifier/)                      |
| Python     | `.py`                        | [`autopep8`](https://pypi.org/project/autopep8/)                              |
| SQL        | `.sql`                       | [`sqlparse`](https://pypi.org/project/sqlparse/)                              |

For Python, `style50` follows [PEP 8](https://peps.python.org/pep-0008/), except that it allows lines of up to 100 characters (rather than 79), consistent with CS50's style guide for C. To see the list of supported file extensions yourself, execute `style50 -E`.

## Source Code

<https://github.com/cs50/style50>
