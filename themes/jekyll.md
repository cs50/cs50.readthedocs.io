# Jekyll

## Configuration

### `Gemfile`

To use CS50's theme, it suffices to configure your `Gemfile` as follows:

```text
source "https://rubygems.org/"

gem "jekyll-theme-cs50", group: :jekyll_plugins, git: "https://github.com/cs50/jekyll-theme-cs50", branch: "develop"
```

### `_config.yml`

CS50's theme can be configured via a `cs50` key in `_config.yml` (or another YAML file), the value of which is an object with any of the following keys.

DEFAULTS, OVERRIDES, PLUGINS

#### `alert`

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

#### `assign`

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

#### `description`

To define the site's description, use a `description` key like:

```text
cs50:
  description: Introduction to Computer Science
```

The value of `description` will then be used as the site's `og:description` value.

#### `locale`

To define the site's locale (e.g., French), use a `locale` key like:

```text
cs50:
  locale: fr
```

wherein the value of `locale` is a [language subtag](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry). By default, the value of `locale` is assumed to be `en`.

#### `title`

To define the site's title, use a `title` key like:

```text
cs50:
  title: CS50
```

The value of `title` will then be used in the site's `title` tags and `og:title` values, prefixed with each page's own title.

#### `tz`

To define the site's time zone (e.g., Pacific Time), use a `tz` key like

```text
cs50:
  tz: America/Los_Angeles
```

wherein the value is a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). By default, the value of `tz` is assumed to be `America/New_York`.

The value of `tz` is used by CS50's [`local`](#local) tag.

## Plugins

### `after`

TODO

### `alert`

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

### `before`

TODO

### `calendar`

TODO

### `local`

A `local` tag can be used to render a date and time in the user's own time zone, based on their computer's clock. The block expects one argument, a quoted date and time in `YYYY-MM-DD HH:MM` format, which is assumed to be in the time zone specified by `site.cs50.tz`, the value of which is a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), the default value of which is `America/New_York`.

For instance, if the value of `site.cs50.tz` is `America/New_York` (by default or otherwise), then

```text
{% local "1970-01-01 00:00" %}
```

would be parsed as representing midnight, Eastern Time, on January 1, 1970. But it would be rendered for users in their own time zone.

If tags should be assumed to be in some other time zone (e.g., Pacific Time), then `_config.yml` should be configured with YAML like:

```text
cs50:
  tz: America/Los_Angeles
```

### `next`

TODO

### `spoiler`

A `spoiler` block can be used to present a spoiler (e.g., a hint) on which a user must click in order to see more. The block expects one argument, a string on which the user can click; the content of the block can be HTML, Markdown, or text that the user will then see.

For instance,

```text
{% spoiler "Hint" %}
    42
{% endspoiler %}
```

would be rendered in such a way that a user has to click "Hint" in order to see "42".

### `video`

TODO
