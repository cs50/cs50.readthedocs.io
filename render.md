# CS50 Render

CS50 Render is a web app at [render.cs50.io](https://render.cs50.io/) that allows you to render syntax-highlighted PDFs of source code, just as [`render50`](/render50/) allows at a command line. Here's an [example](https://render.cs50.io/hello.pdf). Unlike `render50`, though, you can use CS50 Render without installing any dependencies on your own computer.

You can even render two or three files side by side for comparison's sake. Here's an [example](https://render.cs50.io/hellos.pdf). When documenting cases of [academic dishonesty in CS50](https://cs.harvard.edu/malan/publications/Teaching_Academic_Honesty_in_CS50.pdf), for instance, we render the cases' files side by side and then annotate the PDFs for Harvard's Administrative Boards and Honor Council.

PDFs can be annotated (for free) with:

- [Adobe Reader DC](https://acrobat.adobe.com/us/en/acrobat/pdf-reader.html) on macOS and Windows
- [Evince Document Viewer](https://help.ubuntu.com/community/Evince) on Ubuntu Linux
- [Preview](https://support.apple.com/en-us/HT201740) on macOS

## API

CS50 Render supports, via POST using `multipart/form-data`, these HTTP parameters:

* `file`, an `input` with `type="file"`, the value of which is a file to be rendered.
* `size`, the value of which, if provided, per [developer.mozilla.org/en-US/docs/Web/CSS/@page/size](https://developer.mozilla.org/en-US/docs/Web/CSS/@page/size), specifies the size of the page to render.
* `y`, which, if provided (with any value), indicates that the files should be rendered side by side.

An HTTP request to CS50 Render must contain one or more values for `file`. But if `y` is present, the request must contain no more than three such values, as only two or three files can be rendered side by side.

A request can be submitted via HTML with:

```html
<form action="https://render.cs50.io/" enctype="multipart/form-data" method="post">
    <input multiple name="file" type="file">
    <input name="y" type="checkbox">
    <input type="submit">
</form>
```

A request (with files like `hello.c` and `hello.py`) can be submitted via cURL with:

```text
curl -F "file=@hello.c" -F "file=@hello.py" -o output.pdf https://render.cs50.io/
```

Or, in side-by-side mode, with:

```text
curl -F "file=@hello.c" -F "file=@hello.py" -F "y=" -o output.pdf https://render.cs50.io/
```

A request (with files like `hello.c` and `hello.py`) can be submitted via Python with:

```py
import requests

response = requests.post("https://render.cs50.io/", files=[("file", open("hello.c")), ("file", open("hello.py"))])
with open("output.pdf", "wb") as output:
    output.write(response.content)
```

Or, in side-by-side mode, with:

```py
import requests

response = requests.post("https://render.cs50.io/", data={"y": True}, files=[("file", open("hello.c")), ("file", open("hello.py"))])
with open("output.pdf", "wb") as output:
    output.write(response.content)
```
