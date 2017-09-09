---
layout: left
---

# CS50 IDE

## Introduction

CS50 IDE is a cloud-based Integrated Development Environment powered by [Cloud9](https://c9.io) that features a cloud-based Ubuntu environment. It features a browser-based editor, that supports C syntax highlighting and word completion, a GUI-based GDB debugging, full control over a cloud-based Ubuntu environment, and many more features including themes, customizable layouts, and keyboard shortcuts. Since it's cloud-based, you can continue working on your problem sets even if you use a different computer!

## Getting Started

1. Visit [cs50.io](https://cs50.io).
1. Use your edX, Harvard, or Yale credentials to log in. 
1. Once you log in, you will automatically be forwarded to CS50 IDE! Hereafter, you may simply return to cs50.io to log in and return to CS50 IDE, where all your files and settings are preserved.
1. Ensure your workspace is up-to-date. (See [Updating](#updating)!)

NOTE: Upon logging into CS50 IDE for the first time, you may be prompted (again) for your email address. If so, after providing it, click **Private** under **Hosted workspace**, then click **Create workspace**.

## Working with Files

### Creating Files

There are multiple ways to create a new file in CS50 IDE:

- Click **File > New File**.
- Click on the little ![plus](ide/plus.png) button atop any of the open panes and choose **New File** to open a blank file in that particular pane.
- From the file browser on the left, right-click or control-click on a directory and choose **New File** from the menu to create a blank file inside that directory, then double-click that file to open it.
- Press <kbd>Alt</kbd> + <kbd>N</kbd> (on a PC) or <kbd>⌘</kbd> + <kbd>N</kbd> (on a Mac).

TIP: There are also provided file templates. For example, to open a `.c` template, click **File > New From Template > C** and save yourself some keystrokes!

### Saving Files

When a file is open in a tab and you have some unsaved changes, CS50 IDE will show a red dot a top that tab, until you save your changes. Probably the easiest way to save a file is to press <kbd>Ctrl</kbd> + <kbd>S</kbd> (on a PC) or <kbd>⌘</kbd> + <kbd>S</kbd> (on a Mac), but you can also achieve the same by clicking **File > Save** (or **File > Save As...** if you want to save that as a new file), while you're working on that file.

![red dot](ide/unsaved.png)

### Downloading Files

To download a file from your workspace to your local computer, simply navigate to the location of that file, in the file browser on the left, right-click on that file's name, and choose **Download**.

To download all files in your workspace, click **File > Download Project**.

### Uploading Files

To upload a file from your local computer to your workspace:

1. Select a directory where you want your files to get uploaded into, by clicking on that directory in the file browser on the left. By default, this is going to be your `~/workspace` directory.
1. Click **File > Upload Local Files...**, then choose either **Select files** or **Select folder**, depending on what you want to upload.

### File Revision History

While working on a file, you can easily undo changes by clicking **Edit > Undo** or by hitting <kbd>Ctrl</kbd> + <kbd>Z</kbd> (on a PC) or <kbd>⌘</kbd> + <kbd>Z</kbd> on your keyboard. Similarly, you can redo changes by clicking **Edit > Redo** or by hitting <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Z</kbd>.

The CS50 IDE also keeps track of file revisions, in case you want to toggle between file revisions, without having to undo or redo many times. You can show the whole file revision history by clicking **File > Show File Revision History**, which will show a timeline similar to the following, on which you can click to jump to a particular version.

![revision history](ide/history.png)

## Working with Terminals

Terminals allow you to interact with the underlying Ubuntu environment of CS50 IDE, using textual commands, to do all sorts of things, such as creating, copying, or moving files, compiling and running your programs, and more.

### Opening New Terminals

When CS50 IDE first starts, there should be a terminal tab open at the bottom, by default. You can also open a new terminal tab in that or any other pane of your choice by clicking the ![plus](ide/plus.png) button atop that pane, and choosing **New Terminal**. Alternatively, you may just hit <kbd>Alt</kbd> + <kbd>T</kbd> (on a PC) or <kbd>Option</kbd> + <kbd>T</kbd> (on a Mac).

By default, the current working directory (CWD) in a new terminal is your `~/workspace` directory. You can always navigate to your desired directory using `cd path/to/directory`.

TIP: To open a terminal in a different directory, navigate to that directory in your file browser, right-click (on a PC) or Ctrl-click (on a Mac) on the directory's name, and choose **Open Terminal Here**.

### Copying and Pasting

You will probably need to copy and paste commands into terminal tabs to run them. By default, copying and pasting via menus will work inside CS50 IDE only (you might even get warned), so it's recommended to use your keyboard to copy and paste by hitting <kbd>Ctrl</kbd> + <kbd>C</kbd> and <kbd>Ctrl</kbd> + <kbd>C</kbd>> (on a PC) or <kbd>⌘</kbd> + <kbd>C</kbd> and <kbd>⌘</kbd> + <kbd>V</kbd> (on a Mac).

### Command History

You will be often using the same commands over and over. Whether you don't remember a particular command, or too lazy to type it again, you can leverage the command history that is kept by your terminals. You can scroll up and down through the list of commands by hitting your keyboard's up or down arrow.

Additionally, you can search for a particular command by hitting <kbd>Ctrl</kbd> + <kbd>R</kbd> (on a PC) or <kbd>⌘</kbd> + <kbd>R</kbd> (on a Mac), then hitting the same again to scroll through the matches, then hitting <kbd>Tab</kbd> to select a particular match to modify it before running or <kbd>Enter</kbd> if you want to run it directly.

### Clearing Terminals

From time to time you will need to clear your terminal so that it's easier to see what you're doing. There are two main ways to do that

1. Press <kbd>Ctrl</kbd> + <kbd>L</kbd> (on a PC) or <kbd>⌘</kbd> + <kbd>L</kbd> (on a Mac). This way doesn't actually clear the terminal, but rather just scrolls down, so you can always scroll back up and see what got cleared, if you wanted to.
1. Press <kbd>Ctrl</kbd> + <kbd>K</kbd> (on a PC) or <kbd>⌘</kbd> + <kbd>K</kbd> (on a Mac). This way actually clears the terminal; you won't be able to scroll back up and see what got cleared.

### Restarting Terminals

Sometimes you need to restart your terminals, for example after an update (see *<<updating-ide>>*), to have the new changes reflected on your terminal tabs. While you could go ahead and close any open terminal tabs, then reopen them, there's an easier way by right-clicking (on a PC) or Control-clicking (on a Mac) inside of any terminal tab and choosing *Restart All Terminal Sessions*.

### Troubleshooting

If you want to force a program to quit, for example because it's stuck in an infinite loop, press <kbd>Ctrl</kbd> + <kbd>C</kbd> (on a PC) or <kbd>⌘</kbd> + <kbd>C</kbd> (on a Mac). It may take several seconds for the program to respond, so do be patient!

As a last resort, in case the program won't stop, you might need to forcibly kill it. Perhaps the easiest way to do that is to just close the terminal tab, clicking *Close* when prompted, and opening a new one.

Alternatively, you can click the stats button (showing memory, CPU, and disk stats) on the upper-right corner, and click *Show Process List*, find your program in the list, select it, and click **Kill**. If it doesn't respond within a few seconds, click *Force Kill* instead.


## Layouts and Themes

### Layouts

The CS50 IDE is very customizable when it comes to laying out panes and tabs. You could very easily split a pane horizontally or vertically, by right-clicking (on a PC) or Ctrl-clicking (on a Mac) somewhere next to the ![plus](ide/plus.png) button atop the pane you want to split and choosing **Split Pane in Two Rows** or **Split Pane in Two Columns**.

![vertical panes](ide/layout.png)

You could also move tabs between different panes by dragging and dropping a tab to the targeted pane or even to somewhere you want a new pane with that tab to be created.

### Themes

There's a number of themes available in CS50 IDE that you can find under **View > Themes**. By default a theme called **Cloud9 Day** is selected, but if you prefer a dark theme, you can select it via **View > Night Mode**. Otherwise, you're free to select from any of the available themes.

![night mode](ide/night-mode.png)

### Presentation Mode

CS50 IDE also provides **Presentation Mode** in which the user interface is even more simplified and font sizes are larger. You can toggle that mode via **View > Presentation Mode**.

![presentation mode](ide/presentation.png)

## Sharing Your Workspace

### Code Sharing

You can easily share code snippets as GitHub gists by highlighting the lines you want to share and clicking the ![octocat](ide/octocat.png) button on the left. Do be reasonable, per CS50's policy on academic honesty.

![gist](ide/gist.png)

### Adding Users to Your Workspace

Sometimes it's useful to share your workspace with someone (e.g. your teacher or TF) to assist you with something. If using the online IDE, and you have the username or email of the user with whom you want to share your workspace, use the **Share** button near the upper-right corner, type that username or email in the text field under **Invite People** and click **Invite**.

### Removing Users from Your Workspace

To remove a user from your workspace, click on the *Share* button near the upper-right corner, then click on the ![remove user](ide/remove.png) button next to the name of that user, in the *Who has access* section, and confirm by clicking **Remove member** when prompted.

### Sharing Your Workspace Domain

By default, your workspace domain is private. But you may want your workspace domain to be publicly accessibly, for example, if you want to demonstrate a web app hosted in your workspace to your teacher, TF, fellow students, friends, or even people on the internet. To do that, click the *Share* button on the upper-right corner, and check the box that says *Public*, in front of *Application*.

TIP: The URL next to **Application** is your workspace's fully-qualified domain name, but you can also print it by running `hostname50` or open it in a new browser tab by clicking **CS50 IDE > Web Server**.

## Updating the IDE

To ensure your workspace is up-to-date, click inside any open terminal tab (or open a new one), type `update50` and hit <kbd>Enter</kbd>.

## Reporting Problems

If having any problems with CS50 IDE, please contact <sysadmins@cs50.harvard.edu> with all the necessary information about the problem, and how to replicate it, attaching screenshot(s) if need be!
