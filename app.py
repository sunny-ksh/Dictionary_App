# API target:
# https://api.dictionaryapi.dev/api/v2/entries/en/hello
from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
import requests
import json, os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap(app)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if len(request.form["word"]) > 0:
            word1 = request.form["word"]
            return redirect(url_for("find", word=word1), 301)
    return render_template("index.html")

@app.route("/find/", methods=["POST", "GET"])
def find():
    word = request.args.get("word")
    url="https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    response = requests.get(url)
    result = json.loads(response.text)[0]

    return render_template("find.html", result = result,
                           current_word=word)

# if __name__ == '__main__':
#     app.run()
