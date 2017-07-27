import os

from flask import Flask, abort, redirect, request, send_file
from raven.contrib.flask import Sentry

# application
app = Flask(__name__)

# monitoring
sentry = Sentry(app)

# no-cache
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# path to _site
_site = os.path.realpath("_site")

# GET /*
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    p = os.path.realpath(os.path.join(_site, path))
    if not p.startswith(_site):
        abort(403)
    if os.path.isfile(p):
        basename = os.path.basename(path)
        if basename == "index.html":
            return redirect(os.path.dirname(path))
        elif basename.endswith(".html"):
            return redirect(os.path.splitext(path)[0])
        else:
            return send_file(p)
    elif os.path.isfile(p + ".html") and os.path.basename(p) != "index":
        return send_file(p + ".html")
    elif os.path.isdir(p):
        if os.path.isfile(os.path.join(p, "index.html")):
            if path.endswith("/") and path != "/":
                return redirect(path[:-1])
            else:
                return send_file(os.path.join(p, "index.html"))
        else:
            abort(403)
    else:
        abort(404)
    return p
