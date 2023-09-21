import csv

from flask import Flask
import requests


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


@app.route("/mean")
def mean() -> str:  # LibreOffice = 127.079_421_160_8; Python = 127.079_421_160_799_16;
    total = 0
    count = 0

    with open("./hw.csv", mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            try:
                total += float(row[2])
                count += 1
            except IndexError:
                pass

    average = total / count

    return str(average)


@app.route("/space")
def space() -> int:
    try:
        url = "http://api.open-notify.org/astros.json"

        response = requests.get(url)
        data = response.json()
        total_astronauts = data.get("number", 0)

        return str(total_astronauts)
    except Exception as e:
        print(e)
        return 0
