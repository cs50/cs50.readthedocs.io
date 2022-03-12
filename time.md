# CS50 Time Converter

CS50 Time Converter is a web app at [time.cs50.io](https://time.cs50.io/) that converts (dates and) times to users' own time zones, as might be helpful for deadlines and events for teachers and students in different time zones. Its landing page supports manual input in numerous [formats](#formats), and its [API](#api) allows for links to specific (dates and) times. It guesses a user's time zone on a user's first visit but allows for manual override, remembering a user's selection thereafter.

## Formats

CS50 Time Converter's landing page supports inputs [in over 200 language locales plus numerous formats](https://dateparser.readthedocs.io/en/latest/introduction.html), among them:

* Wednesday, December 31, 1969, 7:00 PM EST
* Wed, 31 Dec 1969 19:00:00 EST
* Wed, 31 Dec 1969 19:00:00 -0500

- Dec 31, 1969 7:00 PM in Eastern Time (US and Canada)
- Dec 31, 1969 7:00 PM Eastern Time (US and Canada)

* 1969-12-31 19:00
* 19691231T190000-0500
* 1969-12-31T19:00:00-05:00

- tomorrow at 1:37 PM
- tomorrow at 1:37pm
- tomorrow at 13:37

* tuesday at noon
* tue at noon

- 19700101T000000Z
- 19700101T000000+0000
- 1970-01-01T00:00:00Z
- 1970-01-01T00:00:00+00:00
- Thu, 01 Jan 1970 00:00:00 +0000
- Thu, 01 Jan 1970 00:00:00 GMT

* Dec 31, 1969 12:00 AM Eastern Time (US and Canada) 

## API

### Paths

CS50 Time Converter supports URLs of the forms

* `https://time.cs50.io/{start}`
* `https://time.cs50.io/{start}/{end}`
* `https://time.cs50.io/{start}/{duration}`
* `https://time.cs50.io/{duration}/{end}`

where each of `{start}` and `{end}` is a [combined date and time](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) in ISO 8601 format, and `{duration}` is a [duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) in ISO 8601 format. It is not necessary to encode any `+` therein as `%2B`.

A deadline or an event with no end time might thus use the form `https://time.cs50.io/{start}`.

For instance, all of the below represent Tue, 19 Jan 2038 03:14:07 +0000, using UTC:

* <https://time.cs50.io/20380119T031407Z>
* <https://time.cs50.io/2038-01-19T03:14:07Z>
* <https://time.cs50.io/2038-01-19T03:14:07+0000>
* <https://time.cs50.io/2038-01-19T03:14:07+00:00>

And all of the below represent the same, Mon, 18 Jan 2038 10:14:07 -0500, using Eastern Standard Time:

* <https://time.cs50.io/20380118T101407-0500>
* <https://time.cs50.io/2038-01-18T10:14:07-0500>
* <https://time.cs50.io/2038-01-18T10:14:07-05:00>

An event with an end time might use any of `https://time.cs50.io/{start}/{end}`, `https://time.cs50.io/{start}/{duration}`, and `https://time.cs50.io/{duration}/{end}`.

For instance, all of the below represent an interval from Thu, 01 Jan 1970 00:00:00 +0000 until Tue, 19 Jan 2038 03:14:07 +0000:

* <https://time.cs50.io/19700101T000000Z/20380119T031407Z>
* <https://time.cs50.io/1970-01-01T00:00:00Z/2038-01-19T03:14:07Z>
* <https://time.cs50.io/1970-01-01T00:00:00Z/2038-01-19T03:14:07+0000>
* <https://time.cs50.io/1970-01-01T00:00:00Z/2038-01-19T03:14:07+00:00>
* <https://time.cs50.io/19700101T000000Z/P24855DT3H14M>
* <https://time.cs50.io/P24855DT3H14M/20380119T031407Z>

Times converted via CS50 Time Converter's landing page standardize on the shortest of these forms, omitting hyphens (`-`) and colons (`:`). 

Combined dates and times without an offset are assumed to be in America/New_York.

### Query Strings

#### start, end, zone

CS50 Time Converter also supports URLs of the forms

* `https://time.cs50.io/?start={start}`
* `https://time.cs50.io/?start={start}&zone={zone}`
* `https://time.cs50.io/?start={start}&end={end}`
* `https://time.cs50.io/?start={start}&end={end}&zone={zone}`

where `start` and `end` are in any of the [formats](#formats) supported by CS50 Time Converter's landing page, and `zone` is any of the time zones supported by the same. Each of `{start}` and `{end}` will be assumed to be in `zone` unless a time zone or offset is specified in `{start}` or `{end}` itself. Values of `{start}` and `{end}` without a specified time zone or offset are assumed to be in America/New_York if no `zone` is provided.

#### title

CS50 Time Converter also supports URLs of the form

* `https://time.cs50.io/{start}?title={title}`
* `https://time.cs50.io/{start}/{end}?title={title}`
* `https://time.cs50.io/{start}/{duration}?title={title}`
* `https://time.cs50.io/{duration}/{end}?title={title}`

where `title` is a title for a deadline or event. Not only will the title be displayed to users, it will also be embedded in **Add to Calendar** URLs so that it, too, can be added to users' calendars.

#### location

CS50 Time Converter also supports URLs of the form

* `https://time.cs50.io/{start}?location={location}`
* `https://time.cs50.io/{start}/{end}?location={location}`
* `https://time.cs50.io/{start}/{duration}?location={location}`
* `https://time.cs50.io/{duration}/{end}?location={location}`

where `location` is a location for a deadline or event. Not only will the location be displayed to users, it will also be embedded in **Add to Calendar** URLs so that it, too, can be added to users' calendars.

#### Zoom

Among the formats recognized by CS50 Time Converter's landing page is

```text
Dec 31, 1969 12:00 AM Eastern Time (US and Canada)
```

which is the format used in Zoom's registration emails, which means you can even link to CS50 Time Converter in those by editing the template for your **Registrants Confirmation Email** at <https://zoom.us/account/branding#/emails> to include something like the below:

```text
<#if meetingTime??>
${meetingTime}
<a href="https://time.cs50.io/?start=${meetingTime}">convert to your own time zone</a>
</#if>
```
