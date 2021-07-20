# `submit50`

`submit50` is a command-line tool with which you can submit work (e.g., problem sets) to a course (e.g., CS50). It's based on `git`, a "distributed version control system" that allows you to save different versions of files without having to give each version a unique filename (as you might be wont to do on your own Mac or PC!). Via `submit50` and, in turn, `git` can you thus submit work multiple times (i.e., multiple versions thereof).

When you run `submit50`, your files are "pushed" (i.e., uploaded) to CS50's "organization" (also named "submit50") on [GitHub](https://github.com/), a popular service via which developers (like you!) can share code. Your files are stored in a "repository" (a folder, essentially) to which only you and some of CS50's staff have access (and anyone else to whom you grant access). Your work can thus be reviewed and scored in one central place, whether you wrote it in [CS50 IDE](https://ide.cs50.io/) or elsewhere!

## Installation

1. Install [Python 3.6](/python) or later, if you haven't already.
1. Install [`pip`](/pip), if you haven't already.
1. Install `submit50` itself:
    ```text
    pip3 install submit50
    ```

### Upgrading

```text
pip3 install --upgrade submit50
```

## Usage

```text
usage: submit50 [-h] [--logout] [-v] [-V] slug

positional arguments:
  slug           prescribed identifier of work to submit

optional arguments:
  -h, --help     show this help message and exit
  --logout       logout of submit50
  -v, --verbose  show commands being executed
  -V, --version  show program's version number and exit
```

## Examples

### Submitting with `submit50`

To submit work with `submit50`, `cd` to the work's directory and execute

```text
submit50 slug
```

where `slug` is the unique identifier for the work you're submitting, as prescribed by the course (as in a problem's specification). Although the `slug` might resemble the path to a directory, it's simply a unique identifier, independent of your own work's location. If you've not recently run `submit50` (within the past week), you might be prompted to log in with your GitHub username and password. (Per the [source code](https://github.com/cs50/submit50) for `submit50`, your username and password are sent only to GitHub, not to CS50's own servers.) You will then be prompted to confirm whether you indeed want to submit one or more files from your current directory, unless you're missing one or more required files, in which case `submit50` will instead exit without submitting anything.

#### Via SSH

By default, `submit50` pushes your work to GitHub via HTTPS, which requires your GitHub username and password, which is why `submit50` prompts you for both at least once per week. If you'd prefer not to provide `submit50` with your GitHub username and password at all, you can instead push your work to GitHub via SSH. Configure your workspace on [CS50 IDE](https://ide.cs50.io/) (or your own computer) as follows.

1. [Generate an SSH key and add it to `ssh-agent`](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).
1. [Add the SSH key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).
1. Execute 
   ```text
   ssh -T -p443 git@ssh.github.com
   ```
   to add `ssh.github.com` to the list of known hosts for `ssh`, answering "yes" if prompted whether you're sure you want to continue connecting. If all goes well, you should see the message

    ```text
    Hi <USERNAME>! You've successfully authenticated, but GitHub does not provide shell access.
    Connection to github.com closed.
    ```
  (where `<USERNAME>` is your GitHub username).

Thereafter, you should be able to run `submit50` without ever being prompted for your GitHub username or password. 

### Submitting without `submit50`

If comfortable with `git`, you can submit work without `submit50`. Simply push your work to the expected branch (i.e., the work's prescribed slug which is found in the "How to Submit" section of each project.) of `https://github.com/submit50/jharvard` (or `git@github.com:submit50/jharvard.git`), where `jharvard` is your own GitHub username. To get started, either clone that repository or add it to an existing repository as a remote.

On each such branch, take care to create a `.gitignore` file based on `https://github.com/cs50/checks/raw/master/slug/submit50/exclude`, where `slug` is as before, so that you don't submit files that `submit50` would otherwise ignore.

Note again that the branch should not be `master`, `main`, or the like, and instead be the work's prescribed slug as listed in the project specification.

## Implementation Details

To see how `submit50` uses `git` underneath the hood, execute

```text
submit50 -v slug
```
or

```text
submit50 --verbose slug
```
where `slug` is the unique identifier for the work you're submitting.

## FAQs

### Do I need to provide `submit50` with my GitHub username and password?

Nope, you can instead authenticate [via SSH](#via-ssh).

### If I use `git` locally, will `submit50` affect my local repository?

Nope, `submit50` uses its own `GIT_DIR` (in `/tmp`). It will ignore any `.git` directory that you might have locally.

### How does `submit50` remember my GitHub password?

`submit50` remembers your username and password in RAM using [`git-credential-cache`](https://git-scm.com/docs/git-credential-cache/). Your password is never stored on disk or transmitted elsewhere.

## Source Code

<https://github.com/cs50/submit50>
