# CS50 Video Player

CS50 Video Player is a web app at [video.cs50.io](https://video.cs50.io/) that synchronizes instructional videos (e.g., lectures) with screen recordings so that students can toggle between the two. (Videos must be hosted on [YouTube](https://www.youtube.com/).) The player also provides

* a searchable dropdown menu with hyperlinked captions, if the main video is public and has (English) subtitles, and
* a dropdown menu with hyperlinked chapters, if the main video's description includes a table of contents.

Whenever the player is paused, the browser's URL bar is updated with the timecode (in seconds) at which the video was paused, to facilitate linking to specific moments. And if a student closes the player's tab before finishing a video, the player remembers where they left off and resumes at that timecode when the video is re-visited (provided its URL does not have an explicit `start` parameter).

## Configuration

CS50 Video Player supports URLs of the form

```
https://video.cs50.io/:id
```

where `:id` is the ID of a (main) YouTube video. URLs of that form additionally support, via GET, these HTTP parameters:

* `screen`, which, if present, is the ID of a screen recording to synchronize with the main video. The screen recording and main video must have identical durations (in seconds) and audio tracks.
* `start`, which, if present, is a timecode (in seconds) at which to begin playing a video. It must be non-negative, less than the duraion of the video itself, and less than `end`, if present.
* `end`, which, if present, is a timecode (in seconds) at which to stop playing a video. It must be non-negative, less than the duration of the video itself, and greater than `start`, if present.

For example, <https://video.cs50.io/5azaK2cBKGw?screen=byyRAKSo_dM&start=438>.

If a (main) video has (English) subtitles, they will be automatically imported from YouTube.

If a (main) video has a table of contents in its description, it will be automatically imported (as chapters) from YouTube. A table of contents is defined as two or more lines in a video's description formatted as

```
MM:SS - Chapter
MM:SS - Chapter
...
```

or

```
HH:MM:SS - Chapter
HH:MM:SS - Chapter
...
```

where `Chapter` is the chapter's title.

## Acknowledgements

Special thanks to CS50's friends at [Google](https://www.google.com/) for their support of this app!
