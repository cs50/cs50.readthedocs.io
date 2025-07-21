# style50

`style50` is a command-line tool with which you can check your code for consistency with [CS50's style guide](../style/c/) (for C). If your code isn't styled consistently, `style50` will summarize the changes you should make to your code, as by highlighting in <span class="bg-green p-1 text-white">green</span> characters you should add and highlighting in <span class="bg-red p-1 text-white">red</span> characters you should delete.

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

## Usage

To check your code's style, execute

```text
style50 file
```

where `file` is the (path to some) file whose style you'd like to check.

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
style50 -o split hello.c
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

## Installation

`style50` is already installed for you in [CS50 IDE](https://ide.cs50.io/), so no need to install it yourself; simply use it as directed!

If you'd like to install `style50` on your own Mac or PC, so that you can check your code's style without using CS50 IDE, you'll need a command-line environment:

- If running Linux or the like, you already have one! Open a terminal window in your usual way.
- If running Mac OS, you already have one! Open **Applications > Utilities > Terminal**.
- If running Windows, you'll need to install the [Windows Subsystem for Linux](https://msdn.microsoft.com/commandline/wsl/about), which is only supported on Windows 10. Once installed, [run `bash`](https://blogs.windows.com/buildingapps/2016/03/30/run-bash-on-ubuntu-on-windows/).

To install `style50` within that command-line environment:

1. [Install Python](https://www.python.org/downloads/) 2.7 or higher, if not already installed.

1. Install `pip`, as via

   ```text
   sudo easy_install pip
   ```

   if not already installed.

1. Execute

   ```text
   sudo pip3 install style50
   ```
   to install `style50` itself.

1. Install [Artistic Style 3.0](http://astyle.sourceforge.net/). If running a Debian-based operating system (e.g., Ubuntu Linux), simply run

   ```text
   apt-get update
   apt-get install astyle
   ```

   to install CS50's own compiled version of `astyle`.

## Upgrading

Execute

```text
sudo pip install --upgrade style50
```

to upgrade `style50`, once installed.

## Source Code

<https://github.com/cs50/style50>
