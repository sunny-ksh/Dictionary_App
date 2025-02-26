# API target:
# https://api.dictionaryapi.dev/api/v2/entries/en/hello
from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap5
import requests
import json, os
from dotenv import load_dotenv
from flask_moment import Moment
from datetime import datetime


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap5(app)
moment = Moment(app)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if len(request.form["word"]) > 0:
            word = request.form["word"]
            return redirect(url_for("dictionary", word=word), 301)
    return render_template("index.html",
                           current_time=datetime.utcnow())

@app.route("/dictionary/", methods=["POST", "GET"])
def dictionary():
    word = request.args.get("word")
    url="https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    response = requests.get(url)
    result = json.loads(response.text)[0]

    return render_template("dictionary.html", result = result,
                           current_word=word,
                           current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# if __name__ == '__main__':
#     app.run()
