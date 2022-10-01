# Visual Studio Code for CS50

Visual Studio Code for CS50 is a web app at [code.cs50.io](https://code.cs50.io/) that adapts [GitHub Codespaces](https://github.com/features/codespaces) for students and teachers. It automates the process of creating a [repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories) inside of CS50's [GitHub organization](https://github.com/code50), pushing to it an initial [`.devcontainer.json`](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project), and creating a "codespace," which is a [Docker](https://en.wikipedia.org/wiki/Docker_(software)) "container" in the cloud (akin to your very own virtual server). Ultimately, it allows students to start programming with just a browser, without needing to install or configure anything locally on their own computer. Within their browser is a full-fledged version of [Visual Studio Code](https://code.visualstudio.com/), aka VS Code, including a tabbed text editor, terminal window (connected to a Docker container running [`cs50/codespace`](https://cs50.readthedocs.io/cs50/codespace/)), and graphical file explorer.

You can also [use VS Code locally](#vs-code-desktop), even offline without internet, particularly if feeling more comfortable.

## Git

Because a codespace is already associated with a Git repository in CS50's `code50` organization at <https://github.com/code50>, which is used for automated backups, CS50 effectively disables `git` anytime you're inside of `/workspaces/$RepositoryName` (which is a codespace's default directory), wherein `$RepositoryName` is your (numeric) GitHub ID.

However, you can still use `git` outside of that directory, as by cloning other repositories into `/workspaces` itself. For instance, if you'd like to clone <https://github.com/octocat/Hello-World> into a codespace, you could execute

```
cd /workspaces
git clone https://github.com/octocat/Hello-World
cd Hello-World
```

at which point you could use `git` within that `/workspaces/Hello-World` directory as usual. Note that only `/workspaces/$RepositoryName` will be automatically backed up to CS50's `code50` organization; repositories that you clone into `/workspaces` will not.

## Settings

VS Code supports quite a few [settings](https://code.visualstudio.com/docs/getstarted/settings) via which you can customize a codespace:

1. User settings, which "apply globally to any instance of VS Code you open" and can be applied to codespaces as well via [Settings Sync](https://docs.github.com/en/codespaces/customizing-your-codespace/personalizing-codespaces-for-your-account#settings-sync).
1. Remote settings, which are set by CS50 via `.devcontainer.json` file in a codespace. [Remote settings override User settings](https://code.visualstudio.com/docs/getstarted/settings#_settings-precedence).
1. Workspace settings, which can be set by you via VS Code's GUI (or by editing `.vscode/settings.json` manually). [Workspace settings override Remote settings](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project#creating-a-custom-codespace-configuration).

In other words, in terms of predecence, workspace settings > remote settings > user settings.

If you use VS Code outside of CS50, you might thus want to store most of your settings in User settings (and enable Settings Sync). And if there are any Remote settings set by CS50 that you would like to override, you can do so via Workspace settings.

### Themes

See [code.visualstudio.com/docs/getstarted/themes](https://code.visualstudio.com/docs/getstarted/themes).

### User Interface

See [code.visualstudio.com/docs/getstarted/userinterface](https://code.visualstudio.com/docs/getstarted/userinterface).

## Troubleshooting

### Error Messages

#### Could not register service workers

If using Firefox, [disable Enhanced Tracking Protection](https://support.mozilla.org/en-US/kb/report-breakage-due-blocking), or use a different browser.

#### The workbench failed to connect to the server

If using Firefox, [disable Enhanced Tracking Protection](https://support.mozilla.org/en-US/kb/report-breakage-due-blocking), or use a different browser.

### Shortcuts

* Visit [code.cs50.io/.devcontainer.json](https://code.cs50.io/.devcontainer.json) for the latest version of `.devcontainer.json` (without your time zone).
* Visit [code.cs50.io/codespaces](https://code.cs50.io/codespaces) to access your codespaces in CS50's GitHub organization.
* Visit [code.cs50.io/commits](https://code.cs50.io/commits) to access all of the commits that have been pushed to your repository in CS50's GitHub organization.
* Visit [code.cs50.io/repo](https://code.cs50.io/repo) to access your repository in CS50's GitHub organization.
* Visit [code.cs50.io/restart](https://code.cs50.io/restart) to restart your codespace.
* Visit [code.cs50.io/stop](https://code.cs50.io/stop) to stop your codespace.
* Visit [code.cs50.io/update50.sh](https://code.cs50.io/update50.sh) for the latest version of `update50`.

### Deleting a Codespace

**Deleting a codespace will delete all files and folders therein.** If you are sure you want to delete a codespace:

1. Visit [code.cs50.io/codespaces](https://code.cs50.io/codespaces).
2. Under **Your codespaces**, to the right of `main`, click ***...***, select **Delete**, and click **OK**.

You can then create a new codespace by logging back into [code.cs50.io](https://code.cs50.io/).

## VS Code Desktop

If feeling more comfortable, you can also use VS Code locally:

* [without Docker](#without-docker), but with internet access, so that you can connect to a codespace remotely
* [with Docker](#with-docker), via which you'd run a codespace-like container on your own computer, even without internet access

### Without Docker

To use VS Code locally without Docker, but with internet access, connecting to a codespace remotely:

1. Download and install [VS Code](https://code.visualstudio.com/download) itself on your computer.
1. Install VS Code's [GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces) extension.
1. Visit [code.cs50.io](https://code.cs50.io/), check **Open in VS Code desktop**, and log in as usual; you should be prompted to open the codespace in VS Code itself.

Alternatively, if already logged into a codespace, click the codespace's "hamburger" menu (**☰**) and select **Open in VS Code**.

Alternatively still, if already logged into a codespace, open the codespace's [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette), as via **Ctrl+Shift+P** on Linux, **⇧⌘P** on macOS, and **Ctrl+Shift+P** on Windows, select **>Codespaces: Open in VS Code**.

### With Docker

To use VS Code locally with Docker, running a [codespace-like container](https://code.visualstudio.com/docs/remote/containers) on your own computer, even without internet access, and opening a folder like `foo` therein:

1. Download CS50's latest `.devcontainer.json` file from [raw.githubusercontent.com/cs50/codespace/main/.devcontainer.json](https://raw.githubusercontent.com/cs50/codespace/main/.devcontainer.json), saving it in `foo`. Because the file's name starts with a dot (i.e., period), it might seem to "disappear" when you download it. But, in a terminal window on Linux or macOS, you should see it with `ls -a`, and at a command prompt in Windows, you should see it with `dir /a`.
1. Download, install, and start [Docker](/docker/) on your computer.
1. Download and install [VS Code](https://code.visualstudio.com/download) itself on your computer.
1. Install VS Code's [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
1. Open VS Code's [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette), as via **Ctrl+Shift+P** on Linux, **⇧⌘P** on macOS, and **Ctrl+Shift+P** on Windows, select **>Remote-Containers - Open Folder in Container...**, and open `foo`.

Alternatively, select **>Remote-Containers: Install devcontainer CLI**, and then, in VS Code's terminal window, `cd` to `foo` and execute `devcontainer open .`.

Once the container finishes building and starting, you should find that `foo` is mounted within the container at `/workspaces/foo`.

## Authorization

Visual Studio Code for CS50 is implemented as an [OAuth App](https://docs.github.com/en/developers/apps/getting-started-with-apps/about-apps#about-oauth-apps) that "lets external applications request authorization to private details in a user's GitHub account without accessing their password." When you log into Visual Studio Code for CS50 using your GitHub account, CS50 receives, via a [web application flow](https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#web-application-flow), an "access token" from GitHub (but not your password) via which CS50 can execute certain operations (i.e., API calls) on your behalf.

But you'll first be prompted to "authorize" CS50. Only then will that access token have certain permissions, limited by [scopes](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps). CS50 currently requests these scopes:

* `codespace`, via which CS50 can create and manage [codespaces](https://github.com/features/codespaces) on your behalf
* `repo`, via which CS50 can manage a [repository](https://docs.github.com/en/repositories) for you and accept your invitation thereto
* `user:email`, via which CS50 can access the email address with which you've registered for GitHub, but not your actual emails

Note that scopes are not as granular as would be ideal. The `codespace` scope technically allows CS50 to manage any of your codespaces, not just the one(s) you use for C550. And the `repo` scope technically allows CS50 to access any of your repositories, not just the one(s) you use for CS50. In practice, CS50 only uses those scopes to manage CS50-specific resources. But if you have any concerns, you are welcome to create a (separate) GitHub account that you only use for CS50!

## Acknowledgements

Special thanks to CS50's friends at [GitHub](https://github.com/) and [Microsoft](https://www.microsoft.com/) for their support of this app!
