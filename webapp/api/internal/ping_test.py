def test_post_model(app):
    assert app.get("/api/internal/ping").get_data(as_text=True) == "pong"
