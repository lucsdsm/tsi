from flask import Flask
from flask import request
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        print(usuario)
        print(senha)
    else:
        return render_template('login.html')