---
layout: top
---

# `submit50`

`submit50` is a command-line tool with which you can submit work (e.g., problem sets) to CS50. It's based on `git`, a "distributed version control system" that allows you to save different versions of files without having to give each version a unique filename (as you might be wont to do on your own Mac or PC!). Via `submit50` and, in turn, `git` can you thus submit work multiple times (i.e., multiple versions thereof).

When you run `submit50`, your files are "pushed" (i.e., uploaded) to [GitHub](https://github.com/), a popular service via which developers (like you!) can share code. Your files are stored in a "repository" (a folder, essentially) to which only you and some of CS50's staff have access (and anyone else to whom you grant access). Your work can thus be reviewed and scored in one central place, whether you wrote it in [CS50 IDE](https://cs50.io/) or on your own Mac or PC!

## Usage

To submit work with `submit50`, `cd` to the work's directory and execute

```
submit50 slug
```

where `slug` is the unique identifier for the work you're submitting, as prescribed by the course (as in a problem's specification). Although the `slug` might resemble the path to a directory, it's simply a unique identifier, independent of your own work's location. If you've not recently run `submit50`, you may be prompted to log in with your GitHub username and password. You will then be prompted to confirm whether you indeed want to submit one or more files from your current directory, unless you're missing one or more required files, in which case `submit50` will exit without submitting anything.

## Implementation Details

To see how `submit50` uses `git` underneath the hood, execute

```
submit50 -v slug
```

or

```
submit50 --verbose slug
```

where `slug` is the unique identifier for the work you're submitting.
