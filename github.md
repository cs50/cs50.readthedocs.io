# GitHub

Tools like [check50](/check50/) and [submit50](/submit50/) rely on `git`, a popular tool for saving different versions of code, and [GitHub](https://github.com/), a popular website for saving those versions in the cloud. To push (i.e., save) your code to GitHub using `git`, it used to be possible to log into GitHub via a command line (as in a terminal window) using a GitHub username and password. As of August 13, 2021, that's no longer possible, which means you can no longer use `check50` or `submit50` using your GitHub username and password either.

But you can still use `check50` and `submit50`! You just need to log in a bit differently.

## SSH

1. Open a terminal window (as in CS50 IDE).
1. Execute `ssh-keygen`. When prompted to "save the key," just hit Enter, without typing anything.
1. When prompted to enter a "passphrase," optionally type a passphrase (i.e., password) that you won't forget, then hit Enter, then type it again, then hit Enter again. For security's sake, you won't see what you type. You'll then see a "randomart image" that you can ignore.
1. Execute `cat ~/.ssh/id_rsa.pub`. You'll then see your "public key," multiple lines of seemingly random text. Highlight and copy all of those lines, from `ssh-rsa` to the end. **But don't highlight your terminal window's prompts (which contain `$`) before or after those lines.**
1. Visit [https://github.com/settings/keys](https://github.com/settings/keys), logging in with your GitHub username and password as usual. Don't use you the passphrase you just created, if any.
1. Click **New SSH Key**.
1. Paste your public key into the text box under **Key**. Optionally type a title under **Title** (e.g., `CS50 IDE` if using CS50 IDE).
1. Click **Add SSH Key**.

You should now be able to use `check50` and `submit50` (and `git`) without GitHub username and password. But if you created a passphrase, you might still be prompted for that.

