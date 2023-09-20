# CS50 Manual Pages

CS50 Manual Pages is a web app at [manual.cs50.io](https://manual.cs50.io/) that simplifies (some of) the manual pages for the C standard library and C POSIX library for students less comfortable by providing explanations for (some) functions' synopses, descriptions, return values, and examples. It includes all of the functions in [these header files](https://pubs.opengroup.org/onlinepubs/9699919799/idx/head.html) but only simplifies those that students are likely to use in CS50 itself.

Underneath the hood, the web app uses [pandoc](https://pandoc.org/) to convert Linux's manual pages to HTML and [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) to modify them.
