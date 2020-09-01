# CS50 Vault

CS50 Vault is a web app at [vault.cs50.io](https://vault.cs50.io/) that allows you to add authentication to any link, requiring that users authenticate via **edX**, **GitHub**, **HarvardKey**, **Princeton CAS**, or **Yale CAS** in order to access it, thereby allowing you to post a link online while still restricting access.

Upon authenticating, a user will be redirected to the link, unless the link can be rendered in an `iframe`, in which case its URL will be masked. Alternatively, if the link is to a:

* file on **dropbox.com**, the link can be customized to trigger an automatic download of the file
* folder on **dropbox.com**, the link can be customized to trigger an automatic download of a ZIP of the folder
* video on **youtube.com** (or **youtu.be**), the link can be customized to embed the video in an `iframe` such that it fills the user's window and autoplays

## Notes

* After authenticating, a user could theoretically share a link with anyone on the internet (as via email or any other mechanism), thereby allowing others to access it without authentication. However, once accessed by one user, most any digital asset can be shared with (or copied for) others. CS50 Vault simply raises a bar thereto.
* Embedding a YouTube video in an `iframe` obfuscates, but does not prevent discovery of, the video's underlying URL, which is exposed via HTML. After authenticating, a user could theoretically share that link as well.
* A link will only be rendered in an `iframe` if it
  * is not served with an `X-Frame-Options` header,
  * is not served with an `Content-Security-Policy` header, the value of which contains `frame-ancestors`, and
  * is served with a `Content-Type` header, the value of which is `application/pdf` or `text/html`.
