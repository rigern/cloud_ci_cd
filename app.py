# app.py

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    message = 'ИЛья лох!'
    return render_template('index.html', message=message)
