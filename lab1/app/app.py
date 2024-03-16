from random import randint
from flask import Flask, render_template
from faker import Faker

app = Flask(__name__)
application = app
fake = Faker()

IMAGES_NAMES = ("2d2ab7df-cdbc-48a8-a936-35bba702def5.jpg",
                "6e12f3de-d5fd-4ebb-855b-8cbc485278b7.jpg",
                "7d4e9175-95ea-4c5f-8be5-92a6b708bb3c.jpg",
                "afc2cfe7-5cac-4b80-9b9a-d5c65ef0c728.jpg",
                "cab5b7f2-774e-4884-a200-0c0180fa777f.jpg")

def generate_comments(replies=True):
    comments = []
    for _ in range(randint(1, 3)):
        comment = {"author" : fake.name(),"text": fake.text()}
        if replies:
            comment['replies'] = generate_comments(False)

        comments.append(comment)

    return comments 

def post_gen(index : int):
    return {
        "title": f"Заголовок поста №{index}",
        "author": fake.name(),
        "text": fake.paragraph(nb_sentences=100),
        "date": fake.date_time_between(start_date="-2y", end_date="now"),
        "image_filename": IMAGES_NAMES[index % 5],
        "comments": generate_comments()
    }

post_list = [post_gen(i) for i in range(5)]

@app.route("/")
def index():
    msg = "Главная страница"
    title = "Лабораторная работа №1"
    return render_template("index.html", msg=msg, title=title)

@app.route("/posts/<int:post_index>")
def post(post_index):
    title = f"Пост {post_index}"
    post = post_list[post_index]
    return render_template("post.html", title=title, post=post)

@app.route("/posts")
def posts():
    msg = "Посты"
    title = "Посты"
    return render_template("posts.html", msg=msg, title=title, posts=post_list)

@app.route("/about")
def about():
    msg = "Информация об авторе"
    title = "Об авторе"
    return render_template("about.html", msg=msg, title=title)