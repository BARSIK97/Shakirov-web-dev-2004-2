from flask import Flask, render_template, make_response, request, session, url_for, flash, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

app = Flask(__name__)
app.config.from_pyfile("config.py")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth"
login_manager.login_message = "Для доступа к запрашиваемой странице необходимо пройти процедуру аутентификации"
login_manager.login_message_category = "warning"

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app_users = [
    {"user_id": "1", "login": "user", "password": "qwerty"}
]

class User(UserMixin):
    def __init__(self, user_id, login) -> None:
        self.id = user_id
        self.login = login

@login_manager.user_loader
def load_user(user_id):
    for user in app_users:
        if user_id == user["user_id"]:
            return User(user_id, user["login"])

@app.route("/")
def index():
    session["visits"] = session.get("visits", 0) + 1
    title = "Главная страница"
    return render_template("index.html", title=title)

@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "GET":
        return render_template("login.html")

    login = request.form.get("username", "")
    password = request.form.get("password", "")
    remember = request.form.get("remember", "") == "on"

    for user in app_users:
        if login == user["login"] and password == user["password"]:
            login_user(User(user["user_id"], user["login"]), remember=remember)
            flash(f"Авторизация прошла успешно.", category="success")
            target_page = request.args.get("next", url_for("index"))
            return redirect(target_page)

    flash("Неверный логин или пароль.", category="danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    flash("Вы успешно вышли из аккаунта", "info")
    return redirect(url_for("index"))

@app.route("/secret")
@login_required
def secret():
    return render_template("secret.html", title="Секретная страница")

if __name__ == "__main__":
    app.run(debug=True)
