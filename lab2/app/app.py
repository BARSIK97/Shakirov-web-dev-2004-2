from random import randint
from flask import Flask, render_template, make_response, request

import checkform as checkform

app = Flask(__name__)

OPERATORS = {"+": lambda a, b: a + b,
             "-": lambda a, b: a - b,
             "*": lambda a, b: a * b,
             "/": lambda a, b: a / b if b else "На ноль делить нельзя!"
             }


@app.route("/")
def index():
    url = request.url
    title = "lab1"
    return render_template("index.html", title=title, url=url)


@app.route("/URLpar")
def URLpar():
    title = "Параметры URL"
    return render_template("URLpar.html", title=title, request=request)


@app.route("/headers")
def headers():
    title = "Параметры URL"
    return render_template("headers.html", title=title, request=request)


@app.route("/cookie")
def cookie():
    title = "Параметры URL"
    response = make_response(render_template(
        "cookie.html", title=title, request=request))
    if "cookie" in request.cookies:
        response.delete_cookie("cookie")
    else:
        response.set_cookie("cookie", "1")

    return response


@app.route("/formpar", methods=["GET", "POST"])
def formpar():
    title = "Параметры формы"
    return render_template("formpar.html", title=title, request=request)


@app.route("/phone", methods=["GET", "POST"])
def phone():
    title = "Проверка номера Телефона"
    if request.method == "GET":
        return render_template("phone.html", title=title)
    
    phone = request.form.get("phone", "")
    
    phoneCheckResult = checkform.phonecheck(phone)

    if not phoneCheckResult:
        phone = checkform.phoneformat(phone)
        return render_template("phone.html", title=title, request=request, phoneChecked=True, formattedPhone=phone)
    else:
        return render_template("phone.html", title=title, request=request, phoneChecked=True, error=phoneCheckResult)