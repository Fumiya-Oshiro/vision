import os

import sqlite3

from flask import Flask, render_template, request, redirect, session

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run(debug=True)