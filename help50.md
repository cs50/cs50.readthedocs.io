# `help50`

`help50` is a command-line tool with which you can get help understanding error messages in your terminal window. Rather than something you run yourself, it runs automatically: whenever a command fails, `help50` looks at the command's output. If it recognizes the error, it offers a hint in yellow right below it. If it doesn't, and you're in [CS50 Codespace](https://cs50.dev/), it offers a **help50** button atop your terminal window instead, which you can click to ask the [CS50 Duck](../cs50.ai) to explain the error.

For instance, were you to mistype `ls` as `1s`, you would see

```text
$ 1s
bash: 1s: command not found
Did you mean to run `ls` (which starts with a lowercase L)?
```

wherein the last line is `help50`'s hint. Or were you to try to compile `hello.c` with `make hello.c` instead of `make hello`, you would see

```text
$ make hello.c
make: Nothing to be done for 'hello.c'.
Did you mean to run `make hello` instead?
```

And were you to run a command whose error `help50` doesn't recognize, you would see

```text
$ cat nothere
cat: nothere: No such file or directory
🦆 Click `help50` above for help with that error.
```

along with a **help50** button atop your terminal window. Click it, and the duck will be asked to explain what you ran and what happened. The button disappears once you've clicked it or run another command.

Among the errors that `help50` recognizes are misspelled or miscapitalized commands, running a file instead of compiling it (e.g., `./hello.c`), running a program that you haven't recompiled since editing it, a `cd` or `make` or `python` that refers to a file or directory that's in some other directory, `check 50` instead of `check50`, and a Python file of your own (e.g., `cs50.py`) that "shadows" a module of the same name.

## Usage

Nothing to run! Simply run commands as usual, and help appears when a command fails. `help50` ignores commands that fail without any output (e.g., `grep` that finds no matches) and commands that you interrupt with control-c.

If you're accustomed to running

```text
help50 make hello
```

from earlier versions of `help50`, that still works: it simply runs `make hello` for you, and help appears as it would have anyway.

`help50` also supports a few commands of its own:

| Command | Effect |
|---|---|
| `help50 status` | Reports whether `help50` is `started` or `stopped` in the current terminal window. |
| `help50 stop` | Stops `help50` in the current terminal window. |
| `help50 start` | Starts `help50` again in the current terminal window. |
| `help50 disable` | Keeps `help50` from starting in new terminal windows. |
| `help50 enable` | Undoes `help50 disable`. |
| `help50 is-enabled` | Reports whether `help50` is `enabled` or `disabled`. |

## Installation

`help50` is already installed for you in [CS50 Codespace](https://cs50.dev/), so no need to install it yourself; simply use it as directed!

`help50` is part of [`cs50/cli`](../cs50/cli), CS50's Docker image, so it's also available via [`cli50`](../cli50), though without the **help50** button (and thus the duck), which is a feature of CS50 Codespace.

## Source Code

- <https://github.com/cs50/cli>, for `help50` itself and its helpers
- <https://github.com/cs50/help50.vsix>, for the **help50** button in CS50 Codespace
