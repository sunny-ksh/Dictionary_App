from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
import requests
import json

# API target:
# https://api.dictionaryapi.dev/api/v2/entries/en/hello
app = Flask(__name__)
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
    result = json.loads(response.text)

    for i in range(0,2):
    meaning = result[i]["meanings"][i]["definitions"][i]['definition']
    part_of_speech = result[i]["meanings"][i]['partOfSpeech']
    synonym = result[i]["meanings"][i]["definitions"][i]['synonyms']
    antonym = result[i]["meanings"][i]["definitions"][i]['antonyms']

    return render_template("find.html", meaning=meaning,
                           part_of_speech = part_of_speech,
                           antonym=antonym,
                           synonym=synonym,
                           current_word=word)
