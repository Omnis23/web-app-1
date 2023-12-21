'''
Created by: omnis23
Date started: 12/15/2023

This is a way for me to practice Python Flask, HTML, CSS and
JavaScript by doing my own versin of a website refresh for a
business in my hometown.
'''

from datetime import datetime
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)