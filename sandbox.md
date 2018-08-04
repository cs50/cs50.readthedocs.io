# CS50 Sandbox

CS50 Sandbox is a web app at [sandbox.cs50.io](https://sandbox.cs50.io/), for students and teachers especially, that allows users to

* create temporary programming environments (sandboxes) quickly, without even logging in, and 
* share copies (aka clones) of those sandboxes with others.

For instance, a teacher might

* begin a class by asking students to visit [sandbox.cs50.io](https://sandbox.cs50.io/) and start a sandbox for C with a terminal window and text editor, with a file called `hello.c`, all of which the app's landing page facilitates,
* provide students with a pre-configured link like `https://sandbox.cs50.io/?file=hello.c&window=editor&window=terminal` (perhaps shortened via a URL shortener) that, when visited, would yield the same, or
* provide students with starter code, as by creating a sandbox, editing one or more files, and asking students to clone that sandbox by visiting its unique URL.

CS50 Sandbox is essentially a lightweight version of [CS50 IDE](https://cs50.io/), CS50's web-based integrated development environment. CS50 Sandbox is quicker to start, since it doesn't require authentication, but CS50 Sandbox

* does not offer persistence, insofar as sandboxes are cookie-based and thus lost when cookies are cleared or expired,
* does not have `debug50`, CS50 IDE's graphical debugger for C and Python,
* does not offer [file revision history](https://docs.c9.io/docs/file-revision-history), and
* does not support real-time [collaboration](https://docs.c9.io/docs/share-a-workspace#section-collaboration-features) or chat.

## Configuration

CS50 Sandbox supports, via both GET and POST, these HTTP parameters:

* `file`, which, if present, is a file path to pre-create within the sandbox in `/root/sandbox`. If `window` has a value of `editor` (potentially among other values), that file will also be pre-opened in the code editor, unless the value of `file` includes not only a file name but a parent directory as well.
* `window`, whose value must be at least one of:
  * `browser`, in which case the sandbox will have an embedded browser, pre-configured with an address of `http://localhost:8080/`,
  * `editor`, in which case the sandbox will have a code editor,
  * `terminal`, in which case the sandbox will have a terminal window, and/or
  * `x11`, in which case the sandbox will have an embedded X window.

Values of `browser` and `x11` for `window` are mutually exclusive.

When submitted via POST, each value of `file` can be an actual file encoded as `multipart/form-data`, as via a form like the below:

```html
<form action="https://sandbox.cs50.io/" enctype="multipart/form-data" method="post">
    <input name="file" type="file">
    <input name="window" type="hidden" value="editor">
    <input name="window" type="hidden" value="terminal">
    <input type="submit">
</form>
```

## Notes

* If a user accidentally closes a sandbox and does not recall its unique URL, it can be restarted via a link at the bottom of [sandbox.cs50.io](https://sandbox.cs50.io/).
* The languages and frameworks atop [sandbox.cs50.io](https://sandbox.cs50.io/) not mutually exclusive. The radio buttons only serve to pre-check checkboxes (corresponding to UI features) appropriate for those languages and frameworks. Any language or framework can be used thereafter in any sandbox.

## Related

* [A CS50 Sandbox for Students and Teachers](https://medium.com/@cs50/a-cs50-sandbox-for-students-and-teachers-7331ba257ed6)
