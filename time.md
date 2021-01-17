# CS50 Timer Converter

CS50 Time Converter is a web app at [time.cs50.io](https://time.cs50.io/) that converts times to users' own time zones, as might be helpful for students online for deadlines and events.

## Formats

CS50 Time Converter's landing page supports inputs in these (and other) formats (and languages):

* 19700101T000000Z
* 19700101T000000+0000
* 1970-01-01T00:00:00Z
* 1970-01-01T00:00:00+00:00
* Thu, 01 Jan 1970 00:00:00 +0000
* Thu, 01 Jan 1970 00:00:00 GMT

- 1969-12-31 19:00
- 19691231T190000-0500
- 1969-12-31T19:00:00-05:00

* Wed, 31 Dec 1969 19:00:00 -0500
* Wed, 31 Dec 1969 19:00:00 EST
* Wednesday, December 31, 1969, 7:00 PM EST

- tomorrow at 1:37pm
- tomorrow at 1:37 PM
- tomorrow at 13:37

## API

CS50 Time Converter supports URLs of the forms

* `https://time.cs50.io/:start`
* `https://time.cs50.io/:start/:end`
* `https://time.cs50.io/:start/:duration`
* `https://time.cs50.io/:duration/:end`

where each of `:start` and `:end` is a [combined date and time](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) in ISO 8601 format, and `:duration` is a [duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) in ISO 8601 format.

A deadline or an event with no end time might thus use the form `https://time.cs50.io/:start`.

For instance, all of the below represent Tue, 19 Jan 2038 03:14:07 +0000, using UTC:

* <https://time.cs50.io/20380119T031407Z>
* <https://time.cs50.io/2038-01-19T03:14:07Z>
* <https://time.cs50.io/2038-01-19T03:14:07+0000>
* <https://time.cs50.io/2038-01-19T03:14:07+00:00>

And all of the below represent the same, Mon, 18 Jan 2038 10:14:07 -0500, using Eastern Standard Time:

* <https://time.cs50.io/20380118T101407-0500>
* <https://time.cs50.io/2038-01-18T10:14:07-0500>
* <https://time.cs50.io/2038-01-18T10:14:07-05:00>

An event with an end time might use any of `https://time.cs50.io/:start/:end`, `https://time.cs50.io/:start/:duration`, and `https://time.cs50.io/:duration/:end`.

For instance, all of the below represent an interval from Thu, 01 Jan 1970 00:00:00 +0000 until Tue, 19 Jan 2038 03:14:07 +0000:

* <https://time.cs50.io/19700101T000000Z/20380119T031407Z>
* <https://time.cs50.io/1970-01-01T00:00:00Z/2038-01-19T03:14:07Z>
* <https://time.cs50.io/1970-01-01T00:00:00Z/2038-01-19T03:14:07+0000>
* <https://time.cs50.io/1970-01-01T00:00:00Z/2038-01-19T03:14:07+00:00>
* <https://time.cs50.io/19700101T000000Z/P24855DT3H14M>
* <https://time.cs50.io/P24855DT3H14M/20380119T031407Z>

Combined dates and times without an offset are assumed to be in US/Eastern.

Times converted via CS50 Time Converter's landing page at <https://time.cs50.io/> standardize on the shortest of these forms, omitting hyphens (`-`) and colons (`:`). 
