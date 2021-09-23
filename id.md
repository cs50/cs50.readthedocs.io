# CS50 ID

CS50 ID is CS50's authentication service at [id.cs50.io](https://id.cs50.io/) that lets you authenticate users via [HarvardKey](https://key.harvard.edu/), [Princeton CAS](https://csguide.cs.princeton.edu/publishing/cas), or [Yale CAS](https://developers.yale.edu/cas-central-authentication-service) in your own web app or mobile app. Built atop [Auth0](https://auth0.com/), CS50 ID is an implementation of [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html), a "simple identity layer on top of the [OAuth 2.0](https://tools.ietf.org/html/rfc6749) protocol," which standardizes how you can authenticate users against another service (otherwise known as an identity provider) without asking for their usernames or passwords yourself.

After authenticating a user, CS50 ID will ultimately return an [ID token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken), which is a "digitally signed" JSON object (otherwise known as a [JSON Web Token](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32) or JWT), inside of which will be these keys (otherwise known as [claims](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims)):

* `sub`, a unique identifier for the user;
* `name`, the user's full name, if available; and
* `email`, the user's email address, if available.

If storing users in a SQLite database, you may assume that `sub` will be a `UNIQUE` value of type `TEXT` with no more than 255 characters.

## How to Use

To integrate CS50 ID into an app, you'll first want to create a client (i.e., register your app) at [id.cs50.io](https://id.cs50.io/). You'll need to provide a **Description** for your app as well as a **Redirection URI**, a URL to which CS50 ID should redirect users after authenticating them. Upon creating a client, you'll be provided with a **Client Identifier** and **Client Secret**. CS50 ID will also provide you with some **OpenID Provider Metadata**, which includes a list of endpoints (i.e., URLs). Those values should be all you need to add authentication to your app, particularly if using a library that supports OpenID Connect.

### Python

For instance, here are some sample apps for Python, both of which use [Authlib](https://docs.authlib.org/): 

* [Flask](https://github.com/cs50/id/tree/main/flask), which uses Authlib's [Flask OpenID Connect Client](https://docs.authlib.org/en/latest/client/flask.html#flask-openid-connect-client)
* [Django](https://github.com/cs50/id/tree/main/django), which uses Authlib's [Django OpenID Connect Client](https://docs.authlib.org/en/latest/client/django.html#django-openid-connect-client)

Both apps assume that you've defined three "environment variables", as via the commands below

```text
export CLIENT_ID=...
export CLIENT_SECRET=...
export SERVER_METADATA_URL=...
```

wherein the value of `CLIENT_ID` should be your Client Identifier, the value of `CLIENT_SECRET` should be your Client Secret, and the value of `SERVER_METADATA_URL` should be that of your OpenID Provider Metadata. And it assumes that you've created a client with a Redirection URI of `https://example.com/callback`, where `example.com` is your app's domain name.

### QuickStarts

Because CS50 ID is built atop Auth0, a third-party service, you can actually [follow their instructions](https://auth0.com/docs/quickstarts) to get started. **No need to sign up for an Auth0 account.** Instead, when directed to use the "Auth0 dashboard," log into [id.cs50.io](https://id.cs50.io/) instead for your Client Identifier, Client Secret, and more. No need to configure a "Logout URL" either.

## How It Works

If curious, here's how OpenID Connect and, in turn, OAuth2, work:

* [with web apps](https://auth0.com/docs/flows/concepts/auth-code)
* [with mobile apps](https://auth0.com/docs/flows/concepts/auth-code-pkce)

Odds are a library, though, will automate all of these steps for you!

Within those articles, think of "Auth0 Authorization Server," "Auth0 Tenant," and "Your API" as, collectively, "CS50 ID". 

## Acknowledgements

Special thanks to CS50's friends at [Auth0](https://auth0.com/) for their support of this app!
