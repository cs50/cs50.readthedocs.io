# CS50 ID

CS50 ID (not to be confused with [CS50 IDE](/ide/)) is CS50's authentication service that lets you authenticate users via [HarvardKey](https://key.harvard.edu/) or [Yale CAS](https://developers.yale.edu/cas-central-authentication-service) in your own web app or mobile app. More specifically, CS50 ID is an implementation of [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html), a "simple identity layer on top of the OAuth 2.0 protocol," which standardizes how you can authenticate users against another service (otherwise known as an identity provider) without asking for their usernames or passwords yourself.

Upon authenticating a user, CS50 ID will return an [ID token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken), which is a "digitally signed" JSON object (otherwise known as a [JSON Web Token](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32) or JWT), inside of which will be these keys (otherwise known as [claims](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims)):

* `sub`, a unique identifier for the user;
* `name`, the user's full name, if available; and
* `email`, the user's email address, if available.

To integrate CS50 ID into an app, you'll first want to create a client (i.e., register your app) at [id.cs50.io](https://id.cs50.io/). You'll need to provide a **Description** for your app as well as a **Redirection URI**, a URL to which CS50 ID should redirect users after authenticating them. Upon creating a client, you'll be provided with a **Client Identifier** and **Client Secret**. CS50 ID will also provide you with some **OpenID Provider Metadata**, which includes a list of endpoints (i.e., URLs). Those values should be all you need to add authentication to your app, particularly if using a library that supports OpenID Connect.

For instance, here's [sample Flask app](https://github.com/cs50/id/tree/master/flask) that uses [Authlib](https://docs.authlib.org/en/latest/client/flask.html#flask-openid-connect-client). That app assumes that you've defined three "environment variables", as via the commands below

```
export CLIENT_ID=...
export CLIENT_SECRET=...
export SERVER_METADATA_URL=...
```

wherein the value of `CLIENT_ID` should be your Client Identifier, the value of `CLIENT_SECRET` should be your Client Secret, and the value of `SERVER_METADATA_URL` should be that of your OpenID Provider Metadata. And it assumes that you've created a client with a Redirection URI of `https://example.com/callback`, where `example.com` is your app's domain name.

## How It Works

If curious, here's how OpenID Connect works. Odds are a library, though, will automate all of these steps for you!

Source: [medium.com/@darutk/diagrams-of-all-the-openid-connect-flows-6968e3990660](https://medium.com/@darutk/diagrams-of-all-the-openid-connect-flows-6968e3990660)

### Web Apps

[response_type=code](code.png)

1. You'll first redirect the user to a URL like `https://id50.auth0.com/authorize?response_type=code&client_id=CLIENT_ID&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=openid+profile+email&...`, where `CLIENT_ID` is your Client Identifier, `CLIENT_SECRET` is your Client Secret, and `https://example.com/callback` (URL-encoded as `https%3A%2F%2Fexample.com%2Fcallback`) is your Redirection URI.
1. The user will be prompted to authenticate, as via HarvardKey or Yale CAS.
1. The user will be redirected to a URL like `https://example.com/callback?code=...` (i.e., your Redirection URI, in the query string of which will be a `code`).
1. You'll submit that `code` via POST to a URL like `https://id50.auth0.com/oauth/token`.
1. In the response will be an ID token.

## Mobile Apps

[response_type=id_token](id_token.png)

1. You'll first open (in an embedded browser) a URL like `https://id50.auth0.com/authorize?response_type=id_token&client_id=CLIENT_ID&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=openid+profile+email&...`, where `CLIENT_ID` is your Client Identifier, `CLIENT_SECRET` is your Client Secret, and `https://example.com/callback` (URL-encoded as `https%3A%2F%2Fexample.com%2Fcallback`) is your Redirection URI.
1. The user will be prompted to authenticate, as via HarvardKey or Yale CAS.
1. The user will be redirected to a URL like `https://example.com/callback#id_token=...` (i.e., your Redirection URI, in the fragment identifier of which will be an `id_token`).
