#py -3 -m venv .venv
#.venv\Scripts\activate
# pip install flask
# python -m flask --app <arquivo> run --debug

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, das!</p>"