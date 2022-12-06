from flask import Flask, request, jsonify
import json
import urllib.request

app = Flask(__name__)

CACHE = {}


def get_article_details(q, num):
    # https://docs.python.org/3/library/json.html
    # This library will be used to parse the JSON data returned by the API.
    # gnews doc - https://gnews.io/docs/v4?python#introduction

    apikey = ""  # add gnews api key here
    url = f"https://gnews.io/api/v4/search?q=%s&token=%s&max=%s" % (q, apikey, num)

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]
        return articles


@app.route("/search")
def search_news():
    if request.args['q'] in CACHE:
        return jsonify(CACHE[request.args['q']])
    data = get_article_details(request.args['q'], request.args['number'])
    CACHE[request.args['q']] = data
    return jsonify(CACHE[request.args['q']])
