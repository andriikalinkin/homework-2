from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>This is a home page of Homework_3</h1>"


@app.route("/requirements")
def requirements() -> str:
    with open("./requirements.txt", mode="r", encoding="utf-8") as file:
        data = file.readlines()

    requirements_text = "<br>".join(data)

    return requirements_text
