import flask

import request_globals

def init():
    request_globals.app = flask.Flask("webapp")

    import api.main
    api.main.load_all_handlers()

if __name__ == "__main__":
    init()
    request_globals.app.run()
