# Teacher Sites
This is where all the resources for your CS50 classroom will live for your classroom. With this model, you have complete control over what content is displayed as well as how it is displayed.

## Getting Started
1) [Sign up](https://github.com/join) or [login](https://github.com/login?return_to=%2Fjoin) to your GitHub account and visit <https://github.com/cs50/ap>
2) Click the `Fork` button in the top right corner of the page. This will create your own copy of our teacher site, which will live at `https://github.com/USERNAME/ap`, where USERNAME is your own GitHub username.
3) Go to `https://github.com/USERNAME/ap/settings`, where USERNAME is your own username. Scroll down to the GitHub Pages section. Under source, select “Master Branch” and click save.
Within a few minutes your course site should be live at `https://USERNAME.github.io/ap`

## Structure and Organization of Repository
Most files you will be interacting with, particularly if you are less comfortable, are markdown (.md) files. [Markdown](https://www.markdownguide.org/basic-syntax) is a lightweight markup language that allows to you to format text that will later be converted to HTML when your site is built. You can also type HTML snippets directly into your .md files. For example if you wanted to include an iframe for a youtube video. You could literally type `<iframe src="https://www.youtube.com/embed/…"></iframe>` and it will create the iframe on your page. 

### `_includes/`
  * `header.md`: This is where you will set the title and subtitle for your own site.

  * `nav.md`: This is where you will add menu items to your sidebar. 

Note that `*` creates an item in the navigation bar on the left and `***` creates a horizontal divide.

### `assets/pdfs` 
This folder contains all the PDFs used in the CS50 AP curriculum. You do not need to edit any of these files. If interested, all of the reference sheets and a few other miscellaneous PDFs live here. 

### `periods/`
If you have multiple CS50 classes running at different paces, this is where each individual period’s content goes. One method for displaying content is to include all of the units and just comment out what you do not want your students to view like in `1.md` or `5.md`. Be sure to link these in `_includes/nav.md` so that they appear in your nav bar. HTML comments, `<!-- like this -->`, work in .md just make sure you have a blank line between the end of your displayed text and the start of your comment. Otherwise Markdown will print out the plaintext `<!-- … -->` on your website.

### `units/`
The units directory contains an .md file of each unit, which is essential an index of all the specific topics for that unit. Within each unit folder are all of the .md files on the topics for that unit. For example, unit0.md is a list of links to other .md files for all the topics in Unit 0, and within the `unit0/` directory you will find all of those linked .md files for the topics like `computers_and_computing.md` and `how_computers_work.md`.

### `Gemfile` and `_config.yml`
These are files that you do not need to edit. Our teacher sites use a tool called Jekyll, which uses a theme and .md files to create static sites. These files are used by Jekyll to determine how the site should be built.

### `index.md`
This is the markdown file for the homepage of your site, `https://USERNAME.github.io/ap`. You can use this page for most anything including but limited to: course-wide announcements, Twitter feeds, embedded Google Calendars, links to school specific resources etc.

### `tools.md`
This page has a pdf of the workflow for how students typically use CS50 tools. This page also includes usage of CS50-specific command-line tools. If you have created your own tools or would like to share tools you have found to be helpful for your students you can feel free to post them here.

### `syllabus.md`
This page has a lightweight version of our course syllabus along with the fully mapped course syllabus available for download. You can feel free to add additional policies or practices you use to this page.

## Content Updates
You are more than welcome to change the files in this repository in whatever way you see fit. If we make updates to the content or add additional resources, we’ll send along the text that you can copy and paste into your markdown files to keep your site up to date with the lastest resources. This will likely be sent via email and be posted to our [AP Discuss Forum](https://groups.google.com/a/cs50.net/forum/#!forum/ap-discuss). If you are among those more comfy, you are certainly welcome to [sync your fork](https://help.github.com/articles/syncing-a-fork/) with ours. 

## Editing Files
### Less Comfy
If you are among those less comfy, you can do most everything from GitHub’s web UI. To create a new file, simply click create new file and you can specify the file’s path and type the contents of that file directly into the text editor provided. You could also type the contents in some other text editor and upload the file directly with the upload files button. 

![new file](/teacher_sites/github1.png)

You can also edit existing files. Once you’ve selected the file you’d like to edit, click on the pencil icon at the top right of the page. You’ll be able to make changes in the text editor provided.

![edit](/teacher_sites/github2.png)
 
Once you’re satisfied with your changes, you’ll want to commit them. Commit is GitHub lingo for saving a file. The top text box is the message for your commit. It could be something like “adds link to period4.md.” These messages are solely for you so don’t worry about being super descriptive. If you’d like to add further text here you can use the second box for a longer explanation but it is optional. Make sure that you have selected “Commit directly to the `master` branch.” Then click “Commit changes.” 
Within a few minutes or so, your site should reflect these changes.

![commit](/teacher_sites/github3.png)

### More Comfy
If you’d like to develop your site locally and run it locally, before committing your changes, you’ll need to do a little setup first.

First you’ll need to check if you have ruby as with `ruby -v` in your terminal window. If you do not have ruby, you can find installation instructions [here](https://www.ruby-lang.org/en/documentation/installation/). 

After you’ve successfully installed Ruby, you’ll need to install [Jekyll](https://jekyllrb.com/docs/), a static site generator. You can do that with the command `gem install jekyll bundler`. Once everything is installed and you’ve cloned your GitHub repo to your machine, you’ll be able to build and view your site locally.

The first time you build your site you will need to run
`bundle install`

Then to serve up your site you’ll run
`bundle exec jekyll serve`

You can view your site at <http://localhost:4000>. Your page will reflect changes you’ve made to files in real time after saving the file and refreshing the page (it may take a minute or so). From there, you `git add`, `git commit`, and `git push` as normal.
