#py -3 -m venv .venv
#.venv\Scripts\activate
# pip install flask
# python -m flask --app <arquivo> run --debug

from flask import Flask, redirect, url_for
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    person = request.args.get('person')
    return render_template('index.html', person=person)

# Criar um dicionário com dados de exemplo para fazer login:
usuarios = {
    'admin': '1234',
    'user1': 'senha1',
    'user2': 'senha2'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario in usuarios and usuarios[usuario] == senha:
            return redirect(url_for('login', person=usuario))
        else:
            print('Login inválido')
    
    person = request.args.get('person')
    return render_template('login.html', person=person)
