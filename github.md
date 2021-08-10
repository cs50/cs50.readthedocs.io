# GitHub

Tools like [check50](/projects/check50/en/latest/) and [submit50](/submit50/) rely on `git`, a popular tool for saving different versions of code, and [GitHub](https://github.com/), a popular website for saving those versions in the cloud. To push (i.e., save) your code to GitHub using `git`, it used to be possible to log into GitHub via a command line (as in a terminal window) using a GitHub username and password. As of [August 13, 2021](https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/), that's no longer possible, which means you can no longer use `check50` or `submit50` using your GitHub username and password either.

But you can still use `check50` and `submit50`! You just need to log in a bit differently, either using [SSH](#ssh) or a [personal access token](#personal-access-token). Odds are you'll find SSH more convenient.

## SSH

1. Open a terminal window (as in CS50 IDE).
1. Execute `ssh-keygen`. When prompted to "save the key," just hit Enter, without typing anything.
1. You'll then be prompted for a "passphrase" (i.e., password). If you only use your GitHub account for CS50, no need to input a passphrase; just hit Enter. Otherwise, input a passphrase (that you won't forget!), then hit Enter, then input it again, then hit Enter again. For security's sake, you won't see what you type. You'll then see a "randomart image" that you can ignore.
1. Execute `cat ~/.ssh/id_rsa.pub`. You'll then see your "public key," multiple lines of seemingly random text. Highlight and copy all of those lines, from `ssh-rsa` to the end. **But don't highlight your terminal window's prompts (which contain `$`) before or after those lines.**
1. Visit [https://github.com/settings/keys](https://github.com/settings/keys), logging in with your GitHub username and password as usual. Don't use the passphrase you just created, if any.
1. Click **New SSH Key**.
1. Paste your public key into the text box under **Key**. Optionally input a title under **Title** (e.g., `CS50 IDE` if using CS50 IDE).
1. Click **Add SSH Key**.
1. Back to the terminal window (as in CS50 IDE), execute `ssh -p443 -T git@ssh.github.com`. If asked whether you're "sure you want to continue connecting," input `yes`, then hit Enter.

You should now be able to use `check50` and `submit50` (and `git`) without GitHub username and password. But if you created a passphrase, you might still be prompted for that.

### If you created a passphrase but forgot it

1. Visit [https://github.com/settings/keys](https://github.com/settings/keys), click **Delete** next to your old SSH key, then click **I understand, please delete this SSH key**.
1. Follow all of the same [SSH](#ssh) steps, above, again. When prompted to "overwrite" (your old key), input `y`, then hit Enter.

## Personal Access Token

1. Visit [https://github.com/settings/tokens](https://github.com/settings/tokens), logging in with your GitHub username and password as usual.
1. Click **Generate new token**.
1. Input a note under **Note** (e.g., `CS50 IDE` if using CS50 IDE).
1. Select **No expiration** (or something shorter) via the drop-down menu under **Note**.
1. Check **repo** under **Select scopes**.
1. Click **Generate token**.
1. Highlight and copy the "personal access token" that appears. Odds are it will start with `ghp_`.
1. Paste that personal access token somewhere safe (e.g., in a password manager).

You should now be able to use `check50` and `submit50` (and `git`) without GitHub username and password. When prompted to log in, use your GitHub username and that personal access token instead of your password.

### If you created a personal access token but forgot it (or it expired)

1. Visit [https://github.com/settings/tokens](https://github.com/settings/tokens), click **Delete** next to your old personal access token, then click **I understand, delete this token**.
1. Follow all of the same [Personal Access Token](#personal-access-token) steps, above, again.
