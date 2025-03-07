from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_URL = "http://api.quotable.io/random"


def get_random_quote():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return {
            "content": data.get("content", "Ошибка загрузки цитаты"),
            "author": data.get("author", "Unknown"),
            "tags": data.get("tags", []),
            "length": data.get("length", 0),
            "dateAdded": data.get("dateAdded", "N/A"),
            "dateModified": data.get("dateModified", "N/A")
        }
    return {"content": "Ошибка загрузки цитаты", "author": "Unknown", "tags": [], "length": 0, "dateAdded": "N/A", "dateModified": "N/A"}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quote")
def quote():
    return jsonify(get_random_quote())


if __name__ == "__main__":
    app.run(debug=True)