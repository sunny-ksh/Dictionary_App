import requests, json
from flask import redirect, render_template, url_for
from .forms import SearchForm

# Return the fetch result as a dictionary type.
def fetch(word: str):
    form = SearchForm()
    try:
        url="https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    except TypeError:
        return None
    response = requests.get(url)
    if ((response.status_code) != 200):
        return None

    result = json.loads(response.text)[0]
    return result

        # return render_template("dictionary.html",
        #                        search_word=word,
        #                        form=form,
        #                        search_status=False)
