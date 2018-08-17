# CS50 Lab

CS50 is a [scaffolding](https://en.wikipedia.org/wiki/Instructional_scaffolding) programming environment at [lab.cs50.io](https://lab.cs50.io/) that enables

* teachers to create step-by-step programming lessons (i.e., labs), providing incremental feedback at each step, and
* students to progress from an empty file (or starter code) to working code, with hints and feedback along the way.

To create a lab as a teacher, all you need is a [GitHub account](https://github.com/join) and a (public or private) [repository](https://help.github.com/articles/create-a-repo/). To log into and work on a lab as a student, all you need is a [GitHub account](https://github.com/join). Neither use case requires familiarity with `git` itself though if or once comfortable with `git`, you can create labs even more quickly via a command line!

CS50 Lab is essentially an enhanced version of [CS50 Sandbox](sandbox), inspired (and supported!) by our friends at [Next XYZ](https://www.next.xyz/), that allows teachers to embed interactive instructions alongside a sandbox. As such, CS50 Lab is, also, essentially a lightweight version of [CS50 IDE](ide) with problems' specifications embedded in students' actual programming environments.

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
1. [Create a file](https://blog.github.com/2012-12-05-creating-files-on-github/) in that repository called `.cs50.yaml`, optionally [inside of one or more directories](https://github.com/KirstieJane/STEMMRoleModels/wiki/Creating-new-folders-in-GitHub-repository-via-the-browser), using GitHub's website. Or create (and push) the same using `git` itself. Configure `.cs50.yaml` per below.
1. Optionally create another file in the same directory as `.cs50.yaml` called `README.md`, configured per below. While technically optional, without this file your lab won't have instructions!
1. Optionally create in or [upload](https://blog.github.com/2016-02-18-upload-files-to-your-repositories/) to that directory (or any descendent thereof) any files you'd like to install in a student's environment (and automatically open in the text editor's tabs).

You can then (assuming no mistakes!) visit `https://lab.cs50.io/:owner/:repo/:branch/:path`, where each of those placeholders is [as above](#cs50-lab), to see your lab!

## Configuration

### `.cs50.yaml`

### `README.md`

TODO

## Examples

### `.cs50.yaml`

#### README, Terminal Window, Text Editor

This configuration is actually the default, so it suffices to use:

```
lab50: true
```

Equivalently, you can use:

```
lab50:
  window:
    - editor
    - readme
    - terminal
```

#### Files

```
lab50:
  files:
    - foo.c
    - foo.h
```

#### Globbing

Asterisks have special meaning in YAML, so take care to quote any strings with wildcards (like `*`):

```
lab50:
  files:
    - "foo.*"
```

### `README.md`

TODO

## Acknowledgements

Special thanks to CS50's friends at [Next XYZ](https://www.next.xyz/) and [Google](https://www.google.com/) for their support of this app!
