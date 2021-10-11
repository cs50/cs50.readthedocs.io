# Visual Studio Code

*Additional documentation coming soon*

## Deleting a Codespace

**Deleting a codespace will delete all files and folders therein.** If you are sure you want to delete a codespace:

1. Visit [github.com/codespaces](https://github.com/codespaces).
2. Under **Owned by code50**, to the right of `main`, click ***...***, select **Delete**, and click **OK**.

You can then create a new codespace by following the instructions at [code.cs50.io/settings](https://code.cs50.io/settings) again.

## Customizing a Codespace

VS Code supports quite a few [settings](https://code.visualstudio.com/docs/getstarted/settings) via which you can customize a codespace:

1. User settings, which "apply globally to any instance of VS Code you open" and can be applied to codespaces as well via [Settings Sync](https://docs.github.com/en/codespaces/customizing-your-codespace/personalizing-codespaces-for-your-account#settings-sync).
1. Remote settings, which are set by CS50 via `.devcontainer.json` file in your codespace.
1. Workspace settings, which can be set by you via VS Code's GUI (or by editing `.vscode/settings.json` manually).

[Remote settings override User settings](https://code.visualstudio.com/docs/getstarted/settings#_settings-precedence). And [Workspace settings override Remote settings](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project#creating-a-custom-codespace-configuration).

If you use VS Code outside of CS50, you might thus want to store most of your settings in User settings (and enable Settings Sync). And if there are any Remote settings set by CS50 that you would like to override, you can do so via Workspace settings.
