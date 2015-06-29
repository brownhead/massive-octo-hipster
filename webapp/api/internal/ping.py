import flask

from request_globals import app

@app.route("/api/internal/ping")
def hello():
    return flask.request.args.get("q", "pong")
