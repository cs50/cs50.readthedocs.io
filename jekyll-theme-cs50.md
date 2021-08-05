# CS50 Theme

## `alert`

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

### Fixed top

To position an alert at the top of every page in a site (so as to catch users' attention), configure `_config.yml` with YAML like

```text
cs50:
  alert: warning
```

(wherein `warning` can also be any other type) and create `_includes/alert.md`, the contents of which will be rendered within the alert.

To configure the alert as dismissible, such that the user can dismiss it once read, configure `_config.yml` with YAML like

```text
cs50:
  alert: warning dismissible
```

instead. A user's `localStorage` will be used to remember which alerts the user has dismissed.

## `local`

A `local` tag can be used to render a date and time in the user's own time zone, based on their computer's clock. The block expects one argument, a quoted date and time in `YYYY-MM-DD HH:MM` format, which is assumed to be in the time zone specified by `site.cs50.tz`, the value of which is a [TZ database name](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), the default value of which is `America/New_York`.

For instance, if `site.cs50.tz` is indeed `America/New_York`, then

```text
{% local "1970-01-01 00:00" %}
```

would be parsed as representing midnight, Easter Time, on January 1, 1970. But it would be rendered for users in their own time zone.

If tags should be assumed to be in some other time zone (e.g., Pacific Time), then `_config.yml` should be configured with YAML like:

```text
cs50:
  tz: America/Los_Angeles
```

## `spoiler`

A `spoiler` block can be used to present a spoiler (e.g., a hint) on which a user must click in order to see more. The block expects one argument, a string on which the user can click; the content of the block can be HTML, Markdown, or text that the user will then see.

For instance,

```text
{% spoiler "Hint" %}
    42
{% endspoiler %}
```

would be rendered as:

```html
<details>
    <summary>Hint</summary>
    42
</details>
