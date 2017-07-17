import os

from flask import Flask, abort, redirect, request, send_file
from raven.contrib.flask import Sentry

# application
app = Flask(__name__)

# monitoring
Sentry(app)

# path to _site
_site = os.path.realpath("_site")

# GET /*
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    p = os.path.join(_site, path)
    if not p.startswith(_site):
        abort(403)
    if os.path.isfile(p):
        return send_file(p)
    elif os.path.isfile(os.path.join(p, ".html")):
        return send_file(os.path.join(p, ".html"))
    elif os.path.isdir(p) and os.path.isfile(os.path.join(p, "index.html")):
        if p.endswith("/"):
            return redirect(path[:-1])
        return send_file(os.path.join(p, "index.html"))
    else:
        abort(404)
    return p
