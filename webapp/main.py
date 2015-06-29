from flask import Flask
import request_globals
request_globals.app = Flask(__name__)

import api.main
api.main.load_all_handlers()

if __name__ == "__main__":
    request_globals.app.run()
