---
layout: left
---

# `submit50`

`submit50` is a command-line tool with which you can submit work (e.g., problem sets) to CS50. It's based on `git`, a "distributed version control system" that allows you to save different versions of files without having to give each version a unique filename (as you might be wont to do on your own Mac or PC!). Via `submit50` and, in turn, `git` can you thus submit work multiple times (i.e., multiple versions thereof).

When you run `submit50`, your files are "pushed" (i.e., uploaded) to CS50's "organization" on [GitHub](https://github.com/), a popular service via which developers (like you!) can share code. Your files are stored in a "repository" (a folder, essentially) to which only you and some of CS50's staff have access (and anyone else to whom you grant access). Your work can thus be reviewed and scored in one central place, whether you wrote it in [CS50 IDE](https://cs50.io/) or elsewhere!

## Usage

### Submitting with `submit50`

To submit work with `submit50`, `cd` to the work's directory and execute

```
submit50 slug
```

where `slug` is the unique identifier for the work you're submitting, as prescribed by the course (as in a problem's specification). Although the `slug` might resemble the path to a directory, it's simply a unique identifier, independent of your own work's location. If you've not recently run `submit50` (within the past week), you might be prompted to log in with your GitHub username and password. (Per the [source code](https://github.com/cs50/submit50) for `submit50`, your username and password are sent only to GitHub, not to CS50's own servers.) You will then be prompted to confirm whether you indeed want to submit one or more files from your current directory, unless you're missing one or more required files, in which case `submit50` will instead exit without submitting anything.

#### Via SSH

By default, `submit50` pushes your work to GitHub via HTTPS, which requires your GitHub username and password, which is why `submit50` prompts you for both at least once per week. If you'd prefer not to provide `submit50` with your GitHub username and password at all, you can instead push your work to GitHub via SSH. Configure your workspace on [CS50 IDE](https://cs50.io/) (or your own computer) as follows.

1. [Generate an SSH key and add it to `ssh-agent`](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).

1. [Add the SSH key to your GitHub acount](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/).

1. Execute

   ```
   git config --global credential.https://github.com/submit50.username jharvard
   ```

   where `jharvard` is your own GitHub username, which should add lines like the below to your `.gitconfig` so that `submit50` knows your GitHub username.

   ```
   [credential "https://github.com/submit50"]
       username = jharvard
   ```

1. Execute 

   ```
   ssh git@github.com
   ```

    to add `github.com` to the list of known hosts for `ssh`, answering "yes" if prompted whether you're sure you want to continue connecting. 

Thereafter, you should be able to run `submit50` without ever being prompted for your GitHub username or password. 

### Submitting without `submit50`

If comfortable with `git`, you can submit work without `submit50`. Simply push your work to the expected branch (i.e., the work's prescribed slug) of `https://github.com/submit50/jharvard` (or `git@github.com:submit50/jharvard.git`), where `jharvard` is your own GitHub username. To get started, either clone that repository or add it to an existing repository as a remote.

On each such branch, take care to create a `.gitignore` file based on `https://github.com/cs50/checks/raw/master/slug/submit50/exclude`, where `slug` is as before, so that you don't submit files that `submit50` would otherwise ignore.

## Installation

`submit50` is already installed for you in [CS50 IDE](https://cs50.io/), so no need to install it yourself; simply use it as directed!

If you'd like to install `submit50` on your own Mac or PC, so that you can submit work without using CS50 IDE, you'll need a command-line environment:

- If running Linux or the like, you already have one! Open a terminal window in your usual way.
- If running Mac OS, you already have one! Open **Applications > Utilities > Terminal**.
- If running Windows, you'll need to install the [Windows Subsystem for Linux](https://msdn.microsoft.com/commandline/wsl/about), which is only supported on Windows 10. Once installed, [run `bash`](https://blogs.windows.com/buildingapps/2016/03/30/run-bash-on-ubuntu-on-windows/).

To install `submit50` within that command-line environment:

1. [Install Python](https://www.python.org/downloads/) 2.7 or higher, if not already installed.

1. Install `pip`, as via 

   ```
   sudo easy_install pip
   ```

   if not already installed.

1. Execute 

   ```
   sudo pip install submit50
   ```
   to install `submit50` itself.

## Upgrading

Execute

```
sudo pip install --upgrade submit50
```

to upgrade `submit50`, once installed.

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

To view the source code for `submit50`, see <https://github.com/cs50/submit50>.

## FAQs

### Do I need to provide `submit50` with my GitHub username and password?

Nope, you can instead authenticate [via SSH](#via-ssh).

### If I use `git` locally, will `submit50` affect my local repository?

Nope, `submit50` uses its own `GIT_DIR` (in `/tmp`). It will ignore any `.git` directory that you might have locally.

### How does `submit50` remember my GitHub password?

So that you need only type it once per week, `submit50` remembers your username and password in RAM using [`git-credential-cache`](https://git-scm.com/docs/git-credential-cache/).
