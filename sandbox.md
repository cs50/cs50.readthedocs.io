# CS50 Sandbox

CS50 Sandbox is a web app at [sandbox.cs50.io](https://sandbox.cs50.io/), for students and teachers especially, that allows users to

* create temporary programming environments (sandboxes) quickly and
* share copies of those sandboxes with others.

For instance, a teacher might

* begin a class by asking students to visit [sandbox.cs50.io](https://sandbox.cs50.io/) and start a sandbox for C with a terminal window and text editor, with a file called `hello.c`, all of which the app's landing page facilitates,
* provide students with a pre-configured link like `https://sandbox.cs50.io/?file=hello.c&window=editor&window=terminal` (perhaps shortened via a URL shortener) that, when visited, would yield the same, or
* provide students with starter code, as by creating a sandbox, editing one or more files, and asking students to clone that sandbox by visiting its unique URL.

CS50 Sandbox is essentially a lightweight version of [CS50 IDE](https://ide.cs50.io/), CS50's web-based integrated development environment, but CS50 Sandbox 

* does not have `debug50`, CS50 IDE's graphical debugger for C and Python,
* does not offer [file revision history](https://docs.c9.io/docs/file-revision-history), and
* does not support real-time [collaboration](https://docs.c9.io/docs/share-a-workspace#section-collaboration-features) or chat.

To use CS50 Sandbox, students and teachers need only have a (free) [GitHub](https://github.com/) account via which to log in.

## API

CS50 Sandbox supports, via both GET and POST, these HTTP parameters:

* `cmd`, which, if present, specifies the command to be run in the sandbox's terminal window (if not `bash`, the default).
* `file`, which, if present, is a file path to pre-create within the sandbox in `/root/sandbox`. If `window` has a value of `editor` (potentially among other values), that file, if not binary, will also be pre-opened in the code editor.
* `window`, which must have a value of `terminal` (so that the sandbox will have a terminal window) and may have additional values of
  * `browser`, in which case the sandbox will have an embedded browser, pre-configured with an address of `http://localhost:8080/`,
  * `editor`, in which case the sandbox will have a code editor, and/or
  * `x`, in which case the sandbox will have an embedded X window.

For GET, then, the shortest supported URL is `https://sandbox.cs50.io/?window=terminal`.

A URL with multiple values for `window`, meanwhile, might be `https://sandbox.cs50.io/?window=editor&window=terminal`.

Values of `browser` and `x` for `window` are mutually exclusive.

Unsupported parameterizations will yield an HTTP status code of 400.

When submitted via POST, each value of `file` can be an actual file encoded as `multipart/form-data`, as via a form like the below:

```html
<form action="https://sandbox.cs50.io/" enctype="multipart/form-data" method="post">
    <input multiple name="file" type="file">
    <input name="window" type="hidden" value="editor">
    <input name="window" type="hidden" value="terminal">
    <input type="submit">
</form>
```

## Related

* [A CS50 Sandbox for Students and Teachers](https://medium.com/@cs50/a-cs50-sandbox-for-students-and-teachers-7331ba257ed6)

## Acknowledgements

Special thanks to CS50's friends at [Google](https://www.google.com/) and [Pluralsight](https://www.pluralsight.com/) for their support of this app!
