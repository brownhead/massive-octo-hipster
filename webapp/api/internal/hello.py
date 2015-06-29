from request_globals import app

@app.route("/api/internal/hello")
def hello():
    return "Hello World!"
