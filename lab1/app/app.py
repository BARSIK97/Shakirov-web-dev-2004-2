from flask import Flask

app = Flask(__name__)
application = app

@app.route('/') #путь до страницы
def index():
    return 'Hellow, world!'