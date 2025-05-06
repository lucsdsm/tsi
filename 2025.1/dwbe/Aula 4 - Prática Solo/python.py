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

# Dicionário de usuários com logins:
admin = {
    'admin': '123'
}

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Se o método for POST, pode ser login ou ação de música
        if 'usuario' in request.form and 'senha' in request.form:
            usuario = request.form['usuario']
            senha = request.form['senha']
            if usuario in admin and admin[usuario] == senha:
                return redirect(url_for('home', person=usuario))
            else:
                return render_template('index.html', invalido=True)
    
    person = request.args.get('person')
    return render_template('home.html', person=person)