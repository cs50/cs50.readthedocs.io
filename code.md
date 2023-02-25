# Visual Studio Code for CS50

Visual Studio Code for CS50 is a web app at [code.cs50.io](https://code.cs50.io/) that adapts [GitHub Codespaces](https://github.com/features/codespaces) for students and teachers. It automates the process of creating a [repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories) inside of CS50's [GitHub organization](https://github.com/code50), pushing to it an initial [`.devcontainer.json`](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project), and creating a "codespace," which is a [Docker](https://en.wikipedia.org/wiki/Docker_(software)) "container" in the cloud (akin to your very own virtual server). Ultimately, it allows students to start programming with just a browser, without needing to install or configure anything locally on their own computer. Within their browser is a full-fledged version of [Visual Studio Code](https://code.visualstudio.com/), aka VS Code, including a tabbed text editor, terminal window (connected to a Docker container running [`cs50/codespace`](https://cs50.readthedocs.io/cs50/codespace/)), and graphical file explorer.

You can also [use VS Code locally](#vs-code-desktop), even offline without internet, particularly if feeling more comfortable.

## Settings

VS Code supports quite a few [settings](https://code.visualstudio.com/docs/getstarted/settings) via which you can customize a codespace:

1. User settings, which "apply globally to any instance of VS Code you open" and can be applied to codespaces as well via [Settings Sync](https://docs.github.com/en/codespaces/customizing-your-codespace/personalizing-codespaces-for-your-account#settings-sync).
1. Remote settings, which are set by CS50 via `.devcontainer.json` file in a codespace. [Remote settings override User settings](https://code.visualstudio.com/docs/getstarted/settings#_settings-precedence).
1. Workspace settings, which can be set by you via VS Code's GUI (or by editing `.vscode/settings.json` manually). [Workspace settings override Remote settings](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project#creating-a-custom-codespace-configuration).

In other words, Workspace settings override Remote settings, and Remote settings override User settings.

If you use VS Code outside of CS50, you might thus want to store most of your settings in User settings (and enable Settings Sync). And if you would like to override any of [CS50's Remote settings](https://code.cs50.io/settings.json), you can do so via Workspace settings.

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

* Visit [code.cs50.io/.devcontainer.json](https://code.cs50.io/.devcontainer.json) for the latest version of CS50's `.devcontainer.json`.
* Visit [code.cs50.io/codespaces](https://code.cs50.io/codespaces) to access your codespaces in CS50's GitHub organization.
* Visit [code.cs50.io/commits](https://code.cs50.io/commits) to access all of the commits that have been pushed to your repository in CS50's GitHub organization.
* Visit [code.cs50.io/repo](https://code.cs50.io/repo) to access your repository in CS50's GitHub organization.
* Visit [code.cs50.io/restart](https://code.cs50.io/restart) to restart your codespace.
* Visit [code.cs50.io/settings.json](https://code.cs50.io/settings.json) for CS50's default settings for VS Code.
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
1. Install VS Code's [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
1. Open VS Code's [command palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette), as via **Ctrl+Shift+P** on Linux, **⇧⌘P** on macOS, and **Ctrl+Shift+P** on Windows, select **>Dev Containers - Open Folder in Container...**, and open `foo`.

Alternatively, select **>Dev Containers: Install devcontainer CLI**, and then, in VS Code's terminal window, `cd` to `foo` and execute `devcontainer open .`.

Once the container finishes building and starting, you should find that `foo` is mounted within the container at `/workspaces/foo`.

## Git

Because a codespace is already associated with a Git repository in CS50's `code50` organization at <https://github.com/code50>, which is used for automated backups, CS50 effectively disables `git` anytime you're inside of `/workspaces/$RepositoryName` (which is a codespace's default directory), wherein `$RepositoryName` is your (numeric) GitHub ID.

However, you can still use `git` outside of that directory, as by cloning other repositories into `/workspaces` itself. For instance, if you'd like to clone <https://github.com/octocat/Hello-World> into a codespace, you could execute

```
cd /workspaces
git clone https://github.com/octocat/Hello-World
cd Hello-World
```

at which point you could use `git` within that `/workspaces/Hello-World` directory as usual. Note that only `/workspaces/$RepositoryName` will be automatically backed up to CS50's `code50` organization; repositories that you clone into `/workspaces` will not.

## GitHub

### Authorization

Visual Studio Code for CS50 is implemented as an [OAuth App](https://docs.github.com/en/developers/apps/getting-started-with-apps/about-apps#about-oauth-apps) that "lets external applications request authorization to private details in a user's GitHub account without accessing their password." When you log into Visual Studio Code for CS50 using your GitHub account, CS50 receives, via a [web application flow](https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#web-application-flow), an "access token" from GitHub (but not your password) via which CS50 can execute certain operations (i.e., API calls) on your behalf.

But you'll first be prompted to "authorize" CS50. Only then will that access token have certain permissions, limited by [scopes](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps). CS50 currently requests these scopes:

* `codespace`, via which CS50 can create and manage [codespaces](https://github.com/features/codespaces) on your behalf
* `read:org`, so that you can use the [GitHub CLI](https://cli.github.com/)
* `repo`, via which CS50 can manage a [repository](https://docs.github.com/en/repositories) for you and accept your invitation thereto, and so that you can use the [GitHub CLI](https://cli.github.com/)
* `user:email`, via which CS50 can access the email address with which you've registered for GitHub, but not your actual emails

Note that scopes are not as granular as would be ideal. The `codespace` scope technically allows CS50 to manage any of your codespaces, not just the one(s) you use for CS50. And the `repo` scope technically allows CS50 to access any of your repositories, not just the one(s) you use for CS50. In practice, CS50 only uses those scopes to manage CS50-specific resources. But if you have any concerns, you are welcome to create a (separate) GitHub account that you only use for CS50!

### Organization Access

When you log into Visual Studio Code for CS50, your codespace is configured with a "token" that has `repo` [scope](https://docs.github.com/en/developers/apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes), which lets `git` (via a [credential helper](https://git-scm.com/docs/gitcredentials#_avoiding_repetition)) access repositories to which your GitHub account has access.

If you try to access a repository that's owned by an [organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations) that has not granted access to Visual Studio Code for CS50, though, `git` might err with "Repository not found." (And `gh` might err with "Could not resolve to a Repository.") To grant (or request) access for that organization, visit [github.com/settings/connections/applications/d1a90a524497a69391fa](https://github.com/settings/connections/applications/d1a90a524497a69391fa). Alternatively, you can configure your codespace to use [SSH](/github/#ssh) or a [personal access token](/github/#personal-access-token) instead, both of which would have access to any repositories to which your GitHub account has access, whether or not owned by an organization.

## FAQs

### I can't type anything in the terminal

If you can't type anything in the terminal, please do the following:

1. Click the Settings icon (the gear icon on the bottom-left icon).
1. Search for **terminal.integrated.gpuAcceleration**.
1. Click **Workspace**.
1. Set it to **off**.

### Getting "command not found" error in terminal

First, double-check that you are typing in the command correctly. Not only must the command be typed exactly as instructed, but spaces and capitalization must be exact as well.

Second, if you are absolutely sure that you are typing the command exactly as it should be and you are still receiving a `command not found` notification, please make sure:

* Your input method does not introduce special characters.
* Your codespace is not currently in recovery mode.
* You are using a codespace provided by CS50.

### Codespaces run into recovery mode

Occasionally, your codespace might run into a "recovery mode" due to service outage, a container creation error, or the `.devcontainer.json` had been modified incorrectly. Most CS50 commands, such as `check50` and `submit50`, will not work and you can't compile your code using CS50 libraries.

In recovery mode, your terminal prompt would look like:

```
@githubUserName -> /workspaces/githubId (master) $
```

Normally, your terminal prompt should look like a sinlge dollar sign:

```
$
```

To get out of the recovery mode, please do the following:

1. Click the "Extensions" icon on the left, search for the "GitHub Codespaces" extension and install it (if not installed)
1. After installing "GitHub Codespaces" extension, press "Command + Shift + P" (if on macOS) or "Ctrl + Shift + P" (if on Windows), and search for "full rebuild", select "Full Rebuild Container" to perform a codespace rebuild.
1. Your codespace will be launched once the rebuild process completes.

If performing the above steps does not resolve the issue, please make sure:

1. There is no ongoing GitHub outage: [githubstatus.com](https://githubstatus.com)
1. You did not modify `.devcontainer.json` or your `.devcontainer.json` file is valid.

If you are unsure if you have accidentally modified the `.devcontainer.json`, please do the following:

Run this command:

```
code /workspaces/$RepositoryName/.devcontainer.json
```

This will open an editor window. Delete all the content in the editor window, and keep the editor open. Open this webpage in a new browser tab or window: [https://code.cs50.io/.devcontainer.json](https://code.cs50.io/.devcontainer.json). Copy-paste all the content from the webpage to your active Codespace editor window, and save all the changes.

Repeat the previous instructions on triggering a full container rebuild.

### Creating a new Codespace

If your codespace repeatedly runs into recovery mode and the above steps do not resolve the issue, you might want to try creating a new codespace:

1. Visit [code.cs50.io/codespaces](https://code.cs50.io/codespaces).
1. Click **Create codespace on main** (the green button).
1. Wait for your codespace to launch.

Please do NOT delete your old codespace unless you are sure all your files have been synced properly with repository at [code.cs50.io/repo](https://code.cs50.io/repo).

### GitDoc failed to sync with backing repository

If GitDoc is showing a GitHub Authentication error, please do the following:

1. Visit [code.cs50.io](https://code.cs50.io/).
1. Click **Login via GitHub**.
1. Click to **Authorize cs50**.
1. Once your codespace is launched, visit [code.cs50.io/restart](https://code.cs50.io/restart).

### Missing files in Codespace

If you believe some of your files might be missing on Codespace, please first check your backing repository:

[github.com/code50](https://github.com/code50)

If you have submitted any assignments via submit50, you can access them at:

[github.com/me50](https://github.com/me50)

You can also download your submitted assignments from Gradescope (if applicable):

[gradescope.com](https://www.gradescope.com/)

## Acknowledgements

Special thanks to CS50's friends at [GitHub](https://github.com/) and [Microsoft](https://www.microsoft.com/) for their support of this app!
