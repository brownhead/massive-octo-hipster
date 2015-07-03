import flask

import request_globals
request_globals.app = flask.Flask("webapp")
app = request_globals.app

import api.main
api.main.load_all_handlers()

if __name__ == "__main__":
    request_globals.app.run()
