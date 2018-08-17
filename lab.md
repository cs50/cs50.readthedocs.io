# CS50 Lab

CS50 is a web app at <lab.cs50.io> that enables

* teachers to create step-by-step programming lessons (i.e., labs), providing incremental feedback at each step, and
* students to progress from an empty file (or starter code) to working code, with hints and feedback along the way.

To create a lab as a teacher, all you need is a [GitHub account](https://github.com/join) and a (public or private) [repository](https://help.github.com/articles/create-a-repo/). To log into and work on a lab as a student, all you need is a [GitHub account](https://github.com/join). Neither use case requires familiarity with `git` itself though if or once comfortable with `git`, you can create labs even more quickly via a command line!

CS50 Lab is essentially an enhanced version of [CS50 Sandbox](sandbox) that allows teachers to embed interactive instructions alongside a sandbox. As such, CS50 Lab is essentially a lightweight version of [CS50 IDE](ide) with problems' specifications embedded in students' actual programming environments.

URLs of labs are of the form `https://lab.cs50.io/:owner/:repo/:branch/:path`, where 

* `:owner` is the lab's owner, a GitHub user or [organization](https://help.github.com/articles/about-organizations/),
* `:repo` is that owner's repository in which the lab's source can be found,
* `:branch` is the branch on which the lab's source can be found in that repository, and
* `:path` is the path to the lab's source on that branch.

The source for a lab like https://lab.cs50.io/cs50/labs/python/mario/ can thus be found in https://github.com/cs50/labs/tree/python/loops/, wherein

* `cs50` is the lab's owner (hey, that's us),
* `labs` is the lab's repository,
* `python` is the lab's branch,
* `loops` is the lab's path, and
* `tree`, heretofore unmentioned, is just a GitHub-specific component via which you can browse that branch and path.

## Creation


