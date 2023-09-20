# CS50 Forms

CS50 Forms is a web app at [forms.cs50.io](https://forms.cs50.io/) that allows you to:

* add authentication to Google Forms, requiring that respondents authenticate via **edX**, **GitHub**, **HarvardKey**, **Princeton CAS**, or **Yale CAS**, thereby allowing you to post a form's URL online while still restricting access
* pre-fill Google Forms with a respondent's name and email address as well as a respondent's edX username, GitHub username, HUID, or NetID, thereby decreasing the probability of typographical errors

Upon authenticating, a respondent will be redirected to a "[pre-filled link](https://support.google.com/docs/answer/2839588?hl=en)" like

```text
https://docs.google.com/forms/d/e/1FAIpQLSeaFUWMKeKJo5225POeCeJXHktJecyStal_sn6nYEb0rOEgYw/viewform?entry.1142694446=username%40example.com&entry.164044587=Full+Name
```

wherein `username%40example.com` (i.e., `username@example.com`) represents the respondent's email address and `Full Name` represents the respondent's full name, values that Google will use to pre-fill the form.

## Notes

* Respondents can still override (i.e., manually change) any pre-filled value. In our experience, respodnents tend not to, unless explicitly asked to, e.g., adjust their full name to reflect a preferred nickname.
* After authenticating, a respondent could theoretically share a form's URL, pre-filled or otherwise, with anyone on the internet (as via email or any other mechanism), thereby allowing others to access the form without authentication. In our experience, respondents tend not to, if only because there isn't much demand for unauthenticated access to the forms in question, which are usually assignments! CS50 Forms simply raises a bar thereto.
