import os

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app, path='/metrics')
APP_NAME = os.getenv("APP_NAME")


@app.get("/")
def index():
    if APP_NAME:
        return f"welcome to {APP_NAME} app 🎉"
    else:
        return "welcome to simple flask app!"


@app.get("/home")
def get_home_page():
    return "home page"


@app.get("/account")
def account():
    return "account page"


@app.post("/payment")
def payment():
    print("update ...")
    return "payment page"


@app.get("/unittests")
def unittests():
    return "unit test page"


@app.get("/health_frontend")
def cluster_health_check():
    return "health check page👌"


if __name__ == "__main__":
    app.run(debug=False)
