# CS50 Lab

CS50 is a programming environment at [lab.cs50.io](https://lab.cs50.io/) for scaffolded learning that enables

* teachers to create step-by-step programming lessons (labs), providing incremental feedback at each step, and
* students to progress from an empty file (or starter code) to working code, with hints and feedback along the way.

To create a lab as a teacher, all you need is a [GitHub](https://github.com/) account and a (public or private) [repository](https://help.github.com/articles/create-a-repo/). To log into and work on a lab as a student, all you need is the former. Neither use case requires familiarity with `git` itself though if or once comfortable with `git`, you can create labs even more quickly via a command line!

CS50 Lab is essentially an extension of [CS50 Sandbox](sandbox) that allows teachers to embed interactive instructions alongside a sandbox. As such, CS50 Lab is, also, essentially a lightweight version of [CS50 IDE](ide/index) with problems' specifications embedded in students' actual programming environments.

URLs of labs are of the form `https://lab.cs50.io/{owner}/{repo}/{branch}/{path}`, where 

* `owner` is the lab's owner, a GitHub user or [organization](https://help.github.com/articles/about-organizations/), on [github.com](https://github.com/),
* `repo` is that owner's repository in which the lab's source can be found,
* `branch` is the branch on which the lab's source can be found in that repository, and
* `path` is the path to the lab's source on that branch.

The source for a lab like [lab.cs50.io/cs50/labs/2019/fall/mario/less/](https://lab.cs50.io/cs50/labs/2019/fall/mario/less/) can thus be found in [https://github.com/cs50/labs/tree/2019/fall/mario/less/](https://github.com/cs50/labs/tree/2019/fall/mario/less/), wherein

* `cs50` is the lab's owner (hey, that's us),
* `labs` is the lab's repository,
* `2019/fall` is the lab's branch,
* `mario/less` is the lab's path, and
* `tree` is just a GitHub-specific trick, sandwiched between `:repo` and `:branch`, via which you can browse that branch and path.

## Creation

To create a lab:

1. [Sign up](https://github.com/join) for a (free) GitHub account, if you don't have one already.
1. [Create a repository](https://github.com/new), if you don't have one (that you'd like to use) already.
1. [Create a file](https://blog.github.com/2012-12-05-creating-files-on-github/) in that repository called `.cs50.yml`, optionally [inside of one or more directories](https://github.com/KirstieJane/STEMMRoleModels/wiki/Creating-new-folders-in-GitHub-repository-via-the-browser), using GitHub's website. Or create (and push) the same using `git` itself. Configure `.cs50.yml` [per below](#cs50yml).
1. Optionally create another file in the same directory as `.cs50.yml` called `README.md`, configured [per below](#cs50yml). While technically optional, without this file your lab won't have instructions!
1. Optionally create in or [upload](https://blog.github.com/2016-02-18-upload-files-to-your-repositories/) to that directory (or any descendent thereof) any files you'd like to install in a student's environment (and automatically open in the text editor's tabs).

You can then (assuming no mistakes!) visit `https://lab.cs50.io/:owner/:repo/:branch/:path`, where each of those placeholders is [as above](#cs50-lab), to see your lab!

## Configuration

### `.cs50.yml`

To define a lab, it suffices to create a file called `.cs50.yml` in the root (or subdirectory) of a branch in a repository that contains, minimally, a top-level `lab50` key, the value of which is `true`:

```text
lab50: true
```

#### `window`

It turns out [the above](#cs50yml) is an abbreviation of (and equivalent to)

```text
lab50:
  window:
    - editor
    - readme
    - terminal
```

wherein

* `editor` signifies that the lab should have an embedded text editor,
* `readme` signifies that the lab has instructions (written in `README.md`), and
* `terminal` signifies that the lab should have an embedded terminal window.

A value of `terminal` (implicit or explicit) is required.

Also available as values for `window` are 

* `browser`, which signifies that the lab should have an embedded browser, and
* `x`, which signifies that the lab should have an embedded X window,

but those two values are mutually exclusive.

It's worth noting that a lab without `readme` is functionally similar to [CS50 Sandbox](sandbox). Whereas sandboxes are intended to be temporary, labs are persistent: if a student logs into a lab and makes changes, those changes will persist indefinitely (unless the student resets the lab).

#### `files`

To install files in students' environments (e.g., `foo.c` and `foo.h`), add a key below `lab50` called `files` (as a sibling of `window`, if explicitly present):

```text
lab50:
  files:
    - !include foo.c
    - !include foo.h
```

That `!include` is a (confusing) feature of [YAML](https://en.wikipedia.org/wiki/YAML); it indeed means "include," not "don't include," as a programmer might otherwise assume.

If those files exist (in the same directory as `.cs50.yml`), they will be copied into students' environments and opened automatically (if recognized as text files). If those files don't exist, they will be created as empty (and opened).

Files (e.g., `bar.c` and `bar.h`) can also be in subdirectories (of whatever directory `.cs50.yml` is in):

```text
lab50:
  files:
    - !include foo/bar.c
    - !include foo/bar.h
```

Alternatively, you can specify subdirectories:

```text
lab50:
  files:
    - !include foo/
```

Globbing is also supported, but asterisks have special meaning in YAML, so take care to quote any strings that have wildcards:

```text
lab50:
  files:
    - !include "foo/*.c"
    - !include "foo/*.h"
```

You can also exclude files, as with:

```text
lab50:
  files:
    - !exclude "*"
    - !include "foo.*"
```

The value of `files` is an ordered list, top to bottom, so the above means that all files are excluded by default but `foo.*` is then included, thereby overriding their exclusion.

#### `cmd`

To specify a command to be run in the sandbox's terminal window (e.g., `python`), add a key below `lab50` called `cmd`:

```text
lab50:
  cmd: python
```

The (implicit) default is:

```text
lab50:
  cmd: bash
```

### `README.md`

A lab's instructions should be written in `README.md` (which must be in the same directory as `.cs50.yml`), using
[GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/). Via CS50-specific "tags" can you add interactive features to those instructions. If present, each should appear on a line of its own but might very work in other contexts too (e.g., in ordered or unordered lists).

Your Markdown can also contain, if need, raw HTML, but not [these tags](https://github.github.com/gfm/#disallowed-raw-html-extension-).

Your Markdown can also contain [emoji](https://www.webfx.com/tools/emoji-cheat-sheet/). <img alt=":slightly_smiling_face:" height="20" src="https://github.githubassets.com/images/icons/emoji/unicode/1f642.png" title=":slightly_smiling_face:" width="20"> 

#### `next`

To paginate a lab's instructions, inserting a **Next** button and hiding, until clicked, everything below it, you can use this tag:

```text
{% next %}
```

You can override the button's label with a quoted string:

```text
{% next "Step 2" %}
```

#### `spoiler`

To provide students with a spoiler, code or information they should only by clicking a **Spoiler** button, you can use these tags:

```text
{% spoiler %}
The Answer to the Great Question... 
Of Life, the Universe and Everything...
Is...
Forty-two.
{% endspoiler %}
```

You can override the button's label with a quoted string. Accordingly, via

```text
{% spoiler "Hint" %}
You're really not going to like it.
{% endspoiler %}
```

could you provide students with a hint. And via 

```text
{% spoiler "Solution" %}
Forty-two.
{% endspoiler %}
```

could you provide students with a solution.

#### `video`

To embed a YouTube video (responsively) in a lab's instructions, you can use this tag, wherein the URL can be any URL of a video on [YouTube](https://www.youtube.com/):

```text
{% video https://www.youtube.com/watch?v=oHg5SJYRHA0 %}
```

## Acknowledgements

Special thanks to CS50's friends at [Google](https://www.google.com/) and [Pluralsight](https://www.pluralsight.com/) for their support of this app!
