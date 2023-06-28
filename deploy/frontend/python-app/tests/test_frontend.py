from app import main


def test_app_exists():
    app = main.app
    assert app is not None


def test_app_route():
    app = main.app

    client = app.test_client()
    response = client.get("/unittests")
    assert response.status_code == 200
    assert response.data == b"unit test page"
