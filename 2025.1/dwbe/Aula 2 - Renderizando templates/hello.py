from flask import Flask, redirect, url_for
from flask import request
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    person = request.args.get('person')
    return render_template('index.html', person=person)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        return redirect(url_for('index', person=usuario))
    else:
        return render_template('login.html')