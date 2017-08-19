---
layout: left
---

# CS50 Server

CS50 Server is a [Docker](https://github.com/cs50/server/blob/master/Dockerfile) image with which you can (easily!) serve websites with, optionally, back ends implemented in JavaScript, PHP, Python, or Ruby. (We use it to serve CS50's own apps on [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)!) Essentially, it's a lightly customized installation of [Passenger](https://www.phusionpassenger.com/library/), an app server, to which we've added support for PHP (for some of CS50's older web apps). It also facilitates configuration of Nginx, the web server used by Passenger in in [Standalone mode](https://www.phusionpassenger.com/library/config/standalone/intro.html),  via two files, `httpd.conf` and `server.conf`. The image itself is based on [Ubuntu 14.04](https://hub.docker.com/_/ubuntu/), a (Linux) operating system.

Once [CS50 IDE](https://cs50.io/) migrates from Ubuntu 14.04 LTS to Ubuntu 16.04 will CS50 Server be migrated as well.

## Usage

Assuming you already have [Docker Engine](https://docs.docker.com/engine/installation/) installed, base your own `Dockerfile` on `cs50/server` as follows, exposing TCP port 8080, the server's default:

```
FROM cs50/server
EXPOSE 8080
```

Then ensure your app is structured as follows.

- If your app's back end is implemented in **Meteor**
    - in bundled/packaged mode, ensure you have a file called `app.js` (your app's entry point file) in the same directory as your `Dockerfile`.
    - in non-bundled/packaged mode, ensure you have a file called `.meteor` in the same directory as your `Dockerfile`.
- If your app's back end is implemented in **Node.js**, ensure you have a file called `app.js` (your app's entry point file) in the same directory as your `Dockerfile`.
- If your website's back end is implemented in **PHP**, ensure that you have a directory called `public` in the same directory as your `Dockerfile`, inside of which are any PHP files meant to be served publicly.
- If your website's back end is implemented in **Python**, ensure you have a (WSGI) file called `passenger_wsgi.py`, formatted [as prescribed](https://www.phusionpassenger.com/library/walkthroughs/start/python.html#the-passenger-wsgi-file), in the same directory as your `Dockerfile`.
- If your website's back end is implemented in **Ruby** (or **Ruby on Rails**), ensure you have a file called `config.ru`, formatted [as prescribed](https://www.phusionpassenger.com/library/deploy/config_ru.html), in the same directory as your `Dockerfile`.
- If your website does not have a back end, only a front end implemented in **HTML** (presumably with CSS and/or JavaScript), ensure that you have a directory called `public` in the same directory as your `Dockerfile`, inside of which are any HTML (and CSS and/or JavaScript) files meant to be served publicly.

## Configuration

### `APPLICATION_ENV`

If you set an environment called `APPLICATION_ENV` to a value of `dev`, as via a `docker-compose.yml` file, CS50 Server (and, in turn, Passenger) will restart your application's back end after every HTTP request (by [creating a temporary file](https://github.com/cs50/server/blob/master/bin/passenger) called `tmp/always_restart.txt`), thereby ensuring that any changes you make to files are noticed (and not cached).

### Entry Point

By default, CS50 Server looks for a file called `app.js`, `config.ru`, `.meteor`, or `passenger_wsgi.py` per its [Usage](#usage). To configure CS50 Server to use some other file as an app's entry point, adjust your `Dockerfile` as follows, where `app_type` is [as prescribed](https://www.phusionpassenger.com/library/config/standalone/reference/#--app-type-app_type) and `startup_file` is the relative path of the file to use.

```
FROM cs50/server
EXPOSE ####
...
CMD passenger start --app-type app_type --startup-file startup_file
```

### Nginx

You can customize CS50 Server's installation of Nginx by adding [directives](http://nginx.org/en/docs/dirindex.html) as follows.

- To add directives to Nginix's `http` context, put them in a file called `http.conf` in the same directory as your `Dockerfile`.
 Do not surround them with `http {` and `}`.
- To add directives to Nginix's `server` context, put them in a file called `server.conf` in the same directory as your `Dockerfile`. Do not surround them with `server {` and `}`.

#### `rewrite`

To redirect `/surprise` (and `/surprise/`) to `https://youtu.be/dQw4w9WgXcQ`, create a file called `server.conf` in the same directory as your `Dockerfile`, the contents of which are as follows.

```
rewrite ^/surprise/?$ https://youtu.be/dQw4w9WgXcQ redirect;
```

To redirect one domain to another (e.g., `www.cs50.harvard.edu` to `cs50.harvard.edu`), create a file called `server.conf` in the same directory as your `Dockerfile`, the contents of which are as follows.

```
if ($http_host = www.cs50.harvard.edu) {
    rewrite (.*) https://cs50.harvard.edu$1;
}
```

#### `try_files`

To route all requests (that aren't for actual files or directories) to `public/index.php`, create a file called `server.conf` in the same directory as your `Dockerfile`, the contents of which are as follows.

```
location / {
    try_files $uri $uri/ /index.php?$query_string;
}
```

To route all requests (that aren't for actual files or directories) to `public/index.html` (as you might for a JavaScript-based single-page app), create a file called `server.conf` in the same directory as your `Dockerfile`, the contents of which are as follows.

```
location / {
    try_files $uri $uri/ /index.html;
}
```

### Port

By default, CS50 Server uses TCP port 8080. To configure CS50 Server to use some other port, adjust your `Dockerfile` as follows, where `####` is your choice of ports:

```
FROM cs50/server
EXPOSE ####
...
CMD passenger start --port ####
```

### Static Files

By default, CS50 Server assumes that your app's static files are in `public`, which is assumed to be in the same directory as your `Dockerfile`. To configure CS50 Server to look in some other directory, configure your `Dockerfile` as follows, where `path/to/directory` is the relative path to that directory:

```
FROM cs50/server
...
CMD passenger start --static-files-dir path/to/directory
```

## Notes

### HTTPS

If CS50 Server detects that it's running behind a load balancer, whereby `X-Forwarded-Proto` (an HTTP header) is set, and the value of that header is `http` (the implication of which is that a client's request used HTTP instead of HTTPS), CS50 Server will redirect the request to use HTTPS.

### Versions

CS50 Server provides the following environments.

| Node.js | 7.6.0 |
| PHP | 7.1 |
| Python | 3.6.0 |
| Ruby | 2.4.0 |
