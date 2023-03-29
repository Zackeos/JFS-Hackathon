
from scraper import *
from flask import Flask, render_template, redirect, request_started, url_for, request, jsonify, session, flash


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("webpage.html")

@app.route('/getwords', methods=["GET",  "POST"])
def getwords():
    if request.method == "POST":
        url = request.get_json(force=True)
        score = scrape(str(url))
        return jsonify(score)

@app.route('/factcheck', methods=["GET",  "POST"])
def factcheck():
    if request.method == "POST":
        data = request.get_json(force=True)
        score = factcheck(data)
        return jsonify(score)



app.run(host='0.0.0.0', port=3000, debug=True)
