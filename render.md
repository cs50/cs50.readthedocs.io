# CS50 Render

CS50 Render is a web app at [render.cs50.io](https://render.cs50.io/) that allows you to render syntax-highlighted PDFs of source code, just as `[render50](/render50/)` allows at a command line. Unlike `render50`, though, you can use CS50 Render without installing any dependencies on your own computer.

You can even render two or three files side by side for comparison's sake. When documenting cases of [academic dishonesty in CS50](https://cs.harvard.edu/malan/publications/Teaching_Academic_Honesty_in_CS50.pdf), for instance, we render the cases' files side by side and then annotate the PDFs for [Harvard's Honor Council](https://honorcouncil.fas.harvard.edu/).

PDFs can be annotated (for free) with:

- [Adobe Reader DC](https://acrobat.adobe.com/us/en/acrobat/pdf-reader.html) on macOS and Windows
- [Evince Document Viewer](https://help.ubuntu.com/community/Evince) on Ubuntu Linux
- [Preview](https://support.apple.com/en-us/HT201740) on macOS

## Configuration

CS50 Render supports, via POST using `multipart/form-data`, these HTTP parameters:

* `file`, which must be an `input` with `type="file"`, which is a file to be rendered.
* `y`, which, if present (with any value), indicates that the files should be rendered side by side.

An HTTP request to CS50 Render must contain one or more values for `file`. But if `y` is present, the request must contain no more than three such values, as only two or three files can be rendered side by side.

A request can be submitted via a form like the below (or via any HTTP client).

```html
<form action="https://render.cs50.io/" enctype="multipart/form-data" method="post">
    <input multiple name="file" type="file">
    <input name="y" type="checkbox">
    <input type="submit">
</form>
```
