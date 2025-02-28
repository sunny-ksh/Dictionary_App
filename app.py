# API target:
# https://api.dictionaryapi.dev/api/v2/entries/en/hello
from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap5
import requests
import json, os
from dotenv import load_dotenv
from flask_moment import Moment
from datetime import datetime
from main.forms import SearchForm
from main.fetch import fetch

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
bootstrap = Bootstrap5(app)
moment = Moment(app)

@app.route("/", methods=["POST", "GET"])
def index():
    word = None
    form = SearchForm()
    if form.validate_on_submit():
        word = form.word.data
        form.word.data = ''
        return redirect(url_for("dictionary", word=word), 301)
    return render_template("index.html", form=form, search_word=word)

@app.route("/dictionary/<word>", methods=["POST", "GET"])
def dictionary(word=None):
    form = SearchForm()
    if form.validate_on_submit():
        word = form.word.data
        form.word.data = ''
        result = fetch(word)
        return redirect(url_for("dictionary", word=word), 301)

    form.word.data = ''
    result = fetch(word)
    return render_template("dictionary.html", result = result,
                       search_word=word,
                       form=form,
                       search_status=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# if __name__ == '__main__':
#     app.run()
