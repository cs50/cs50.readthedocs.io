# CS50 Lab

CS50 is a [scaffolding](https://en.wikipedia.org/wiki/Instructional_scaffolding) programming environment at [lab.cs50.io](https://lab.cs50.io/) that enables

* teachers to create step-by-step programming lessons (i.e., labs), providing incremental feedback at each step, and
* students to progress from an empty file (or starter code) to working code, with hints and feedback along the way.

To create a lab as a teacher, all you need is a [GitHub](https://github.com/) account and a (public or private) [repository](https://help.github.com/articles/create-a-repo/). To log into and work on a lab as a student, all you need is the former. Neither use case requires familiarity with `git` itself though if or once comfortable with `git`, you can create labs even more quickly via a command line!

CS50 Lab is essentially an extension of [CS50 Sandbox](sandbox) that allows teachers to embed interactive instructions alongside a sandbox. As such, CS50 Lab is, also, essentially a lightweight version of [CS50 IDE](ide) with problems' specifications embedded in students' actual programming environments.

URLs of labs are of the form `https://lab.cs50.io/:owner/:repo/:branch/:path`, where 

* `:owner` is the lab's owner, a GitHub user or [organization](https://help.github.com/articles/about-organizations/), on [github.com](https://github.com/),
* `:repo` is that owner's repository in which the lab's source can be found,
* `:branch` is the branch on which the lab's source can be found in that repository, and
* `:path` is the path to the lab's source on that branch.

The source for a lab like [https://lab.cs50.io/cs50/labs/python/mario/](https://lab.cs50.io/cs50/labs/python/mario/) can thus be found in [https://github.com/cs50/labs/tree/python/loops/](https://github.com/cs50/labs/tree/python/loops/), wherein

* `cs50` is the lab's owner (hey, that's us),
* `labs` is the lab's repository,
* `python` is the lab's branch,
* `loops` is the lab's path, and heretofore unmentioned,
* `tree` is just a GitHub-specific trick via which you can browse that branch and path.

## Creation

To create a lab:

1. [Sign up](https://github.com/join) for a (free) GitHub account, if you don't have one already.
1. [Create a repository](https://github.com/new), if you don't have one (that you'd like to use) already.
1. [Create a file](https://blog.github.com/2012-12-05-creating-files-on-github/) in that repository called `.cs50.yaml`, optionally [inside of one or more directories](https://github.com/KirstieJane/STEMMRoleModels/wiki/Creating-new-folders-in-GitHub-repository-via-the-browser), using GitHub's website. Or create (and push) the same using `git` itself. Configure `.cs50.yaml` [per below](#cs50-yaml).
1. Optionally create another file in the same directory as `.cs50.yaml` called `README.md`, configured [per below](#cs50-yaml). While technically optional, without this file your lab won't have instructions!
1. Optionally create in or [upload](https://blog.github.com/2016-02-18-upload-files-to-your-repositories/) to that directory (or any descendent thereof) any files you'd like to install in a student's environment (and automatically open in the text editor's tabs).

You can then (assuming no mistakes!) visit `https://lab.cs50.io/:owner/:repo/:branch/:path`, where each of those placeholders is [as above](#cs50-lab), to see your lab!

## Configuration

### `.cs50.yaml`

To define a lab, it suffices to create a file called `.cs50.yaml` in the root (or subdirectory) of a branch in a repository that contains, minimally, a top-level `lab50` key, the value of which is `true`:

```
lab50: true
```

#### `windows`

It turns out [the above](#cs50-yaml) is an abbreviation of (and equivalent to)

```
lab50:
  windows:
    - editor
    - readme
    - terminal
```

wherein

* `editor` signifies that the lab should have an embedded text editor,
* `readme` signifies that the lab has instructions (written in `README.md`), and
* `terminal` signifies that the lab should have an embedded terminal window.

Also available as values for `windows` are 

* `browser`, which signifies that the lab should have an embedded browser, and
* `x11`, which signifies that the lab should have an embedded X window,

but those two values are mutually exclusive.

A lab must have, as the value of `windows`, at least one of these five values. 

It's worth noting that a lab without `readme` is functionally similar to [CS50 Sandbox](sandbox). Whereas sandboxes are temporary, cookie-based and thus lost when cookies are cleared or expired, labs are persistent: if a student logs into a lab and makes changes, those changes will persist indefinitely (unless the student resets the lab).

#### `files`

To install files in students' environments (e.g., `foo.c` and `foo.h`), add a key below `lab50` called `files` (as a sibling of `windows`, if explicitly present):

```
lab50:
  files:
    - foo.c
    - foo.h
```

If those files exist (in the same directory as `.cs50.yaml`), they will be copied into students' environments and opened automatically (if recognized as text files). If those files don't exist, they will be created as empty (and opened).

Files (e.g., `bar.c` and `bar.h`) can also be in subdirectories (of whatever directory `.cs50.yaml` is in):

```
lab50:
  files:
    - foo/bar.c
    - foo/bar.h
```

Alternatively, you can specify subdirectories:

```
lab50:
  files:
    - foo/
```

Globbing is also supported, but asterisks have special meaning in YAML, so take care to quote any strings that have wildcards:

```
lab50:
  files:
    - "foo/*.c"
   - "foo/*.h"
```

#### `checks`

To specify checks via which students can receive feedback from [`check50`](check50) on their lab, add a key below `lab50` called `checks`, the value of which is those checks' slug:

```
lab50:
  checks: cs50/labs/python/mario
```

That slug can defined in the same `.cs50.yaml` file in which the lab itself is defined, as with:

```
check50: true
```

#### `submit`

To specify a "slug" via which students can submit a lab via [`submit50`](submit50), add a key below `lab50` called `submit`, the value of which is that slug:

```
lab50:
  submit: cs50/labs/python/mario
```

That slug can defined in the same `.cs50.yaml` file in which the lab itself is defined, as with:

```
submit50: true
```

### `README.md`

A lab's instructions should be written in `README.md` (which must be in the same directory as `.cs50.yaml`), using
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/). Via CS50-specific "tags" can you add interactive features to those instructions. If present, each should appear on a line of its own but might very work in other contexts too (e.g., in ordered or unordered lists).

#### `check`

To provide students with a **Check** button via which they can receive automated feedback on a particular check from [`check50`](check50), using the [slug defined in `.cs50.yaml`](#checks), you can use these tags, between which is an object (e.g., `compiles`) that representing that check's result (and the results of any checks on which that check depends):

```
{% check %}
{{ compiles }}
{% endcheck %}
```

You can override the button's label with a quoted string:

```
{% check "Does your code compile?" %}
{{ compiles }}
{% endcheck %}
```

Between those tags can also be logic that inspects the value of objects' properties (e.g., `passed`):

```
{% check "Does your code compile?" %}
{{ if compiles.passed }}
Yes! Nicely done.
{% else %}
{{ compiles }}
{% endif %}
{% endcheck %}
```

Supported logic includes [control flow](https://shopify.github.io/liquid/tags/control-flow/) and [iteration](https://shopify.github.io/liquid/tags/iteration/).

#### `next`

To paginate a lab's instructions, inserting a **Next** button and hiding, until clicked, everything below it, you can use this tag:

```
{% next %}
```

You can override the button's label with a quoted string:

```
{% next "Step 2" %}
```

#### `spoiler`

To provide students with a spoiler, code or information they should only by clicking a **Spoiler** button, you can use these tags:

```
{% spoiler %}
The Answer to the Great Question... 
Of Life, the Universe and Everything...
Is...
Forty-two.
{% endspoiler %}
```

You can override the button's label with a quoted string. Accordingly, via

```
{% spoiler "Hint" %}
You're really not going to like it.
{% endspoiler %}
```

could you provide students with a hint. And via 

```
{% spoiler "Solution" %}
Forty-two.
{% endspoiler %}
```

could you provide students with a solution.

#### `submit`

To display, via a **Submit** button, the command via which students can submit a lab via `submit50`, you can use this tag, provided your `.cs50.yaml` has a value beneath `lab50` for `submit`:

```
{% submit %}
```

You can override the button's label with a quoted string:

```
{% submit "Ready to submit?" %}
```

#### `video`

To embed a YouTube video (responsively) in a lab's instructions, you can use this tag, wherein the URL can be any URL of a video on [YouTube](https://www.youtube.com/):

```
{% video https://www.youtube.com/watch?v=oHg5SJYRHA0 %}
```

## Acknowledgements

Special thanks to CS50's friends at [Next XYZ](https://www.next.xyz/) and [Google](https://www.google.com/) for their support of this app!
