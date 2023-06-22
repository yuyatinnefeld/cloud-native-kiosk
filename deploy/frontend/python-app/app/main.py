import os

from flask import Flask, render_template, redirect, request, url_for
import flask_login
from flask_login import LoginManager, UserMixin

login_manager = LoginManager()

app = Flask(__name__)
app.secret_key = "key"

login_manager.init_app(app)

users = {
    "user": {"pw": "pwd"},
}


class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return
    else:
        user = User()
        user.id = username
        return user


@login_manager.request_loader
def request_loader(request):
    username = request.form.get("username")
    if username not in users:
        return
    else:
        user = User()
        user.id = username
        user.is_authenticated = request.form["pw"] == users[username]["pw"]
        return user


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        if request.form.get("pw") == users[username]["pw"]:
            user = User()

        user.id = username
        flask_login.login_user(user)
        return redirect(url_for("protect"))
    else:
        return render_template("index.html")


@app.route("/logout")
def logout():
    flask_login.logout_user()
    return "Logged out"


@app.route("/home")
@flask_login.login_required
def protect():
    return render_template("home.html")


@app.route("/account")
@flask_login.login_required
def account():
    return render_template("account.html")


@app.route("/unittests")
def unittests():
    return "This is for Unittests"


@app.route("/health_frontend")
def cluster_health_check():
    return "Health check frontend👌"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
