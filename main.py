import csv

from flask import Flask, request, jsonify
from markupsafe import escape
from faker import Faker
import requests


app = Flask(__name__)
fake = Faker()


@app.route("/")
def home():
    return "<h1>This is a home page of Homework_3</h1>"


@app.route("/users/generate")
def users() -> str:
    query = request.args.get("query", default=100, type=int)

    all_users = []

    for _ in range(query):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower() + last_name.lower()}@example.com"

        one_user = f"{first_name} {last_name} {email}"
        all_users.append(one_user)

    return "<br>".join(all_users)


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
def space() -> str:
    try:
        url = "http://api.open-notify.org/astros.json"

        response = requests.get(url)
        data = response.json()
        total_astronauts = data.get("number", 0)

        return str(total_astronauts)
    except Exception as e:
        print(e)
        return str(0)


if __name__ == "__main__":
    app.run()
