# FAQs

## How can I open a file in the editor from a terminal tab?

If you want to open a file named `foo`, run `open path/to/foo`.

## I closed the terminal under my editor by mistake. How do I get it back?

If the Console pane at the bottom is visible, you should be able to open a new terminal tab by clicking the ![plus](plus.png) button atop that pane, and choosing **New Terminal**.

![console pane](console.png)

TIP: If you no longer see the Console pane, you can bring it back via **View > Console** or by hitting <kbd>F6</kbd>. You can also open a terminal in any other pane.

## Can I use a different editor?

Sure, if you are more familiar, you can run editors in the terminal such as `emacs`, `nano`, or `vim`.

## What if I already have a AWS account?

The CS50 IDE isn't available yet to all AWS accounts.

## How to restore files that I have accidentally deleted?

Please follow the instructions at **[How do I recover a deleted file?](https://community.c9.io/t/how-do-i-recover-a-deleted-file/17/2)**. Let sysadmins@cs50.harvard.edu know if you need further assistance!


## How do I free up disk space?

You can free up disk space in your IDE by removing the files that are big in size. To list your files and their sizes, run the following command in the IDE's terminal:

```
du -h /home/ubuntu | grep -v \.c9 | sort -h
```

then (optionally) download copies of these files to your own computer and remove them from your IDE by right- or control-clicking on them and choosing Delete or using the `rm` command in the terminal.
