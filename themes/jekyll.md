# Jekyll

[Jekyll](https://jekyllrb.com/) is a static site generator for which CS50 has its own [theme](https://jekyllrb.com/docs/themes/), which comes with its own [layout](#layout), [includes](#includes), [configuration options](#configuration-options), [plugins](#plugins), and custom [syntax](#syntax). It also supports custom CSS via [Sass](#sass).

The theme uses [Bootstrap](https://getbootstrap.com/) as well as other third-party libraries. 

To use CS50's theme, it suffices to configure your `Gemfile` as follows:

```text
source "https://rubygems.org/"

gem "jekyll-theme-cs50", group: :jekyll_plugins, git: "https://github.com/cs50/jekyll-theme-cs50", branch: "develop"
```

CS50's theme automatically enables some third-party plugins as well, per `PLUGINS` in [https://github.com/cs50/jekyll-theme-cs50/blob/develop/lib/jekyll-theme-cs50/constants.rb](https://github.com/cs50/jekyll-theme-cs50/blob/develop/lib/jekyll-theme-cs50/constants.rb). You can enable other plugins in the `Gemfile` itself.

## Layout

On larger screens (e.g., laptops and desktops), CS50's theme lays out pages as follows, wherein `aside` represents the site's sidebar, `main` represent's a page's content, and `alert` represents an optional alert:

```text
+------------------------+
| alert                  |
+------------------------+
|        |               |
|        |               |
| aside  | main          |
|        |               |
|        |               |
+------------------------+
```

Within each `aside` is a `header`, a `nav`, and a `footer`:

```text
+------------------------+
|                        |
+------------------------+
| header |               |
|        |               |
| nav    |               |
|        |               |
| footer |               |
+------------------------+
```

On smaller screens (e.g., phones), the `aside` is collapsed and relocated up top:

```text
+---------------+
| alert         |
+---------------+
| aside         |
+---------------+
|               |
|               |
| main          |
|               |
|               |
+---------------+
```

When the `aside` is collapsed, only the site's `header` is visible:

```text
+---------------+
|               |
+---------------+
| header        |
+---------------+
|               |
|               |
|               |
|               |
|               |
+---------------+
```

But a button, when clicked, reveals the `nav` and `footer`:

```text
+---------------+
|               |
+---------------+
| header        |
|               |
| nav           |
|               |
| footer        |
+---------------+
|               |
|               |
|               |
|               |
|               |
+---------------+
```

## Includes

CS50's layout automatically includes these files if they exist in `_includes`:

* `alert.md`, the content of which will appear in a top-level [alert](#alert), if `site.cs50.alert` is configured
* `header.md`, the content of which will appear at the top of the theme's `aside`
* `nav.md`, the content of which will appear in the middle of the theme's `aside`
* `footer.md`, the content of which will appear at the bottom of the theme's `aside`

## Configuration Options

CS50's theme can be configured via a `cs50` key in `_config.yml` (or another YAML file), the value of which is an object with these keys:

* [alert](#alert)
* [assign](#assign)
* [description](#description)
* [locale](#locale)
* [title](#title)
* [tz](#tz)

Some of those keys have default values, as do other top-level keys, per `DEFAULTS` in [https://github.com/cs50/jekyll-theme-cs50/blob/develop/lib/jekyll-theme-cs50/constants.rb](https://github.com/cs50/jekyll-theme-cs50/blob/develop/lib/jekyll-theme-cs50/constants.rb).

And some top-level keys have fixed values that cannot be changed in `_config.yml` (or another YAML file), per `OVERRIDES` in [https://github.com/cs50/jekyll-theme-cs50/blob/develop/lib/jekyll-theme-cs50/constants.rb](https://github.com/cs50/jekyll-theme-cs50/blob/develop/lib/jekyll-theme-cs50/constants.rb).

### alert

To position an alert at the top of every page in a site (so as to catch users' attention), use an `alert` key like

```text
cs50:
  alert: warning
```

(wherein `warning` can also be any other type of alert) and create `_includes/alert.md`, the contents of which will be rendered within the alert.

To configure the alert as dismissible, such that the user can dismiss it once read, configure `_config.yml` with YAML like

```text
cs50:
  alert: warning dismissible
```

instead. A user's `localStorage` will be used to remember which alerts the user has dismissed.

### assign

To define a global variable (e.g., `foo`) with some value (e.g., `bar`), user an `assign` key like:

```text
cs50:
  assign:
    foo: bar
```

You can then access that variable in pages with syntax like:

```text
{{ foo }}
```

Or use it conditionally in pages with syntax like:

```text
{% if foo == "bar" %}
    baz
{% endif %}
```

We use `assign` when generating multiple sites from one collection of pages (e.g., for Harvard College and Harvard Extension School), as by defining

```text
cs50:
  assign:
    college: true
```

in one configuration file (e.g., `_college.yml`) and

```text
cs50:
  assign:
    extension: true
```

in another configuration file (e.g., `_extension.yml`) and then using conditional logic in pages like:

```text
{% if college %}
    This is CS50
{% elsif extension %}
    This is CSCI E-50
{% endif %}
```

We then build the sites separately with commands like:

```text
bundle exec jekyll build --config _config.yml,_college.yml --destination _site/college/
```

and:

```text
bundle exec jekyll build --config _config.yml,_extension.yml --destination _site/extension/
```

### description

To define the site's description, use a `description` key like:

```text
cs50:
  description: Introduction to Computer Science
```

The value of `description` will then be used as the site's `og:description` value.

### locale

To define the site's locale (e.g., French), use a `locale` key like:

```text
cs50:
  locale: fr
```

wherein the value of `locale` is a [language subtag](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry). By default, the value of `locale` is assumed to be `en`.

### title

To define the site's title, use a `title` key like:

```text
cs50:
  title: CS50
```

The value of `title` will then be used in the site's `title` tags and `og:title` values, prefixed with each page's own title.

### tz

To define the site's time zone (e.g., Pacific Time), use a `tz` key like

```text
cs50:
  tz: America/Los_Angeles
```

wherein the value is a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). By default, the value of `tz` is assumed to be `America/New_York`.

The value of `tz` is used by CS50's [`local`](#local) tag.

## Plugins

* [after](#after)
* [alert](#alert-1)
* [before](#before)
* [calendar](#calendar)
* [local](#local)
* [spoiler](#spoiler)
* [video](#video)

### after

An `after` block can be used to hide content until a specific date and time. The content of the block can be HTML, Markdown, or text.

For instance,

```text
{% after "2001-01-01 00:00:00" %}
    It is the 21st century
{% endafter %}
```

would not display "It is the 21st century" until it is the 21st century (in the site's time zone).

Note that the content of the block is always present in the browser's DOM and is only hidden via CSS, so this block should not be used to hide sensitive content (e.g., a link to an otherwise accessible exam).

### <plugins/>alert

An `alert` block can be used to render an [alert](https://getbootstrap.com/docs/5.1/components/alerts/). The block expects one argument, the type of alert to render, which can be any of:

* `primary`
* `secondary`
* `success`
* `danger`
* `warning`
* `info`
* `light`
* `dark`

The content of the block can be HTML, Markdown, or text.

### before

A `before` block can be used to show content until a specific date and time. The content of the block can be HTML, Markdown, or text.

For instance,

```text
{% after "2001-01-01 00:00:00" %}
    It is the 20th century
{% endafter %}
```

would display "It is the 20th century" until it is no longer the 20th century (in the site's time zone).

Note that the content of the block is always present in the browser's DOM and is only hidden via CSS, so this block should not be used to hide sensitive content (e.g., a link to an otherwise accessible exam).

### calendar

A `calendar` tag can be used to embed a Google Calendar in "agenda" mode. The tag expects one argument, the "Calendar ID" (i.e., `src`) of a Google Calendar, which appears under "Integrate calendar" in [calendar settings](https://support.google.com/calendar/answer/41207). The calendar must be [public](https://support.google.com/calendar/answer/37083). For instance,

```text
{% calendar en.usa%23holiday@group.v.calendar.google.com %}
```

would embed the Google Calendar whose Calendar ID is `en.usa%23holiday@group.v.calendar.google.com`.

### local

A `local` tag can be used to render dates and times in the user's own time zone, based on their device's clock. The tag can be passed

* one argument, a quoted date and time in `YYYY-MM-DD HH:MM` format, or 
* two arguments, a quoted start date and time in `YYYY-MM-DD HH:MM` format followed by a quoted end date and time in `YYYY-MM-DD HH:MM` format or, if the end time is within 24 hours of the start time, a quoted time in `HH:MM` format, repesenting a range.

Dates and times are assumed to be in the time zone specified by `site.cs50.tz`, the value of which is a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), the default value of which is `America/New_York`.

For instance, if the value of `site.cs50.tz` is `America/New_York` (by default or otherwise), then

```text
{% local "1970-01-01 00:00" %}
```

would be parsed as representing midnight, Eastern Time, on January 1, 1970. But it would be rendered for users in their own time zone. Similarly,

```text
{% local "1970-01-01 00:00" "1970-01-01 23:59" %}
```

and

```text
{% local "1970-01-01 00:00" "23:59" %}
```

would both be parsed as representing a range that begins at midnight, Eastern Time, on January 1, 1970, and ends at 23:59 on the same. But it, too, would be rendered for users in their own time zone. If the value of `site.cs50.locale` is `en`, the range's times will be rendered, when possible, with an n-dash (–).

If tags should be assumed to be in some other time zone (e.g., Pacific Time), then `_config.yml` should be configured with YAML like:

```text
cs50:
  tz: America/Los_Angeles
```

The format in which dates and times should be rendered can be configured with YAML like:

```yaml
cs50:
  local:
    day: numeric
    hour: numeric
    minute: numeric
    month: long
    timeZoneName: short
    weekday: long
    year: numeric
```

Default values for those keys are defined in [https://github.com/cs50/jekyll-theme-cs50/blob/develop/lib/jekyll-theme-cs50/constants.rb](https://github.com/cs50/jekyll-theme-cs50/blob/develop/lib/jekyll-theme-cs50/constants.rb). Other possible values for those keys are defined by the [ECMAScript Internationalization API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat). 

Setting the value of a key to `null` will remove the key from the plugin's output. For instance,

```yaml
cs50:
  local:
    year: null
```

would remove the year from the default format for dates and times.

### spoiler

A `spoiler` block can be used to present a spoiler (e.g., a hint) on which a user must click in order to see more. The block expects one argument, a string on which the user can click; the content of the block can be HTML, Markdown, or text that the user will then see.

For instance,

```text
{% spoiler "Hint" %}
    42
{% endspoiler %}
```

would be rendered in such a way that a user has to click "Hint" in order to see "42".

### video

A `video` tag can be used to embed a YouTube video. The tag expects one argument, the URL of the video to embed. For instance,

```text
{% video https://www.youtube.com/watch?v=xvFZjo5PgG0 %}
```

would embed [https://www.youtube.com/watch?v=xvFZjo5PgG0](https://www.youtube.com/watch?v=xvFZjo5PgG0).

The tag can also be used to embed the same video using [CS50 Video Player](/video/) instead. For instance,

```text
{% video https://video.cs50.io/xvFZjo5PgG0 %}
```

would embed [https://video.cs50.io/xvFZjo5PgG0](https://video.cs50.io/xvFZjo5PgG0) instead.

## Syntax

CS50's theme supports all of [Jekyll](https://jekyllrb.com/docs/)'s and [Kramdown](https://kramdown.gettalong.org/syntax.html)'s syntax and also some of its own for:

* [links](#links)
* [lists](#lists)
* [subtitles](#subtitle)

It also supports [Mermaid](https://mermaid-js.github.io/)'s syntax via fenced code blocks like:

````
```mermaid

```
````

And it supports [scratchblocks](https://en.scratch-wiki.info/wiki/Block_Plugin/Syntax) via fenced code blocks like:

````
```scratch

```
````

### Links

So that Jekyll sites can be deployed to subdirectories on web servers, CS50's theme assumes that absolute paths like `/baz/` refers to a directory called `baz` in the base directory of the Jekyll site, not the web server itself. For instance, if a Jekyll site is deployed to `http://example.com/foo/bar/`, then a Markdown link like

```text
[baz](/baz/)
```

would ultimately link to `http://example.com/foo/bar/baz/` relatively, not to `http://example.com/baz/` absolutely.

To link to a directory in the root of the web server itself, use Markdown like

```text
[baz](http://example.com/baz/)
```

instead.

### Lists

Normally, (unordered) lists can be implemented in Markdown with any of `*`, `+`, and `-`, but CS50's theme treats those symbols as distinct:

* a `*` will be rendered as a bullet as usual
* a `+` will be rendered as a subtree that's collapsed by default
* a `-` will be rendered as a subtree that's expanded by default

For instance, Markdown like

```text
* foo
- bar
    * qux
+ baz
    * quux
```

would be appear initially has having three top-level bullets (foo, bar, and baz), with qux also visible, but if baz were clicked, quux would appear too.

### Subtitle

So that pages can have not only titles but subtitles, CS50's interprets a `##` that immediately follows a `#` heading, with no content in between, as representing a subtitle. For instance, Markdown like

```text
# Title
## Subtitle
```

would be rendered in such a way that "Subtitle" is clearly a subtitle.

## Sass

CS50's theme uses [Sass](https://sass-lang.com/), which means you can customize Bootstrap as well as CS50's own CSS by creating `assets/page.scss` with, at least, these lines, along with your own:

```text
---
---

@import "page";
```

For instance, to override the theme's crimson colors with shades of blue, you could use:

```text
---
---

$link-color: #286dc0;

@import "page";

aside {
    background-color: #00356b;
}
```

## Acknowledgements

CS50's theme is inspired by [Hyde](https://github.com/poole/hyde).
