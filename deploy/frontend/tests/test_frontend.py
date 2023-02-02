import pytest
from flask import Flask

def test_app_exists():
    app = Flask(__name__)
    assert app is not None

def test_app_route():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello, World!"

    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"
