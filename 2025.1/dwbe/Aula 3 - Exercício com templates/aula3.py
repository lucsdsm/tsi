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
    'user2': 'senha2',
    '1': '1'
}

# Criar um dicionário com dados de exemplo para as músicas favoritas:
musicas_favoritas = {
    'admin': ['Imagine', 'Let it Be'],
    'user1': ['Shape of You'],
    'user2': [],
    '1': []
}

@app.route('/home', methods=['GET', 'POST'])
def home():
    # Se o método for POST, pode ser login ou ação de música
    if request.method == 'post':
        # Se for tentativa de login (usuário e senha estão presentes)
        if 'usuario' in request.form and 'senha' in request.form:
            usuario = request.form['usuario']
            senha = request.form['senha']
            if usuario in usuarios and usuarios[usuario] == senha:
                return redirect(url_for('home', person=usuario))
            else:
                return render_template('index.html', invalido=True)

        # Caso contrário, é ação relacionada a música
        person = request.args.get('person')
        
        if person in musicas_favoritas:
            acao = request.form.get('acao')
            musica = request.form.get('musica', '').strip()

            if acao == 'add' and musica:
                musicas_favoritas[person].append(musica)

            elif acao == 'remove' and musica in musicas_favoritas[person]:
                musicas_favoritas[person].remove(musica)

            elif acao == 'editar':
                # Modo de edição: mostrar o campo de edição
                lista_completa = musicas_favoritas.get(person, [])
                return render_template(
                    'home.html',
                    person=person,
                    musicas=lista_completa,
                    busca='',
                    musica_editar=musica
                )

            elif acao == 'editar_salvar':
                original = request.form.get('original', '').strip()
                novo_nome = request.form.get('novo_nome', '').strip()
                if original in musicas_favoritas[person] and novo_nome:
                    index = musicas_favoritas[person].index(original)
                    musicas_favoritas[person][index] = novo_nome

    # GET ou após redirecionamento POST
    person = request.args.get('person')
    busca = request.args.get('busca', '').strip().lower()
    lista_completa = musicas_favoritas.get(person, [])

    if busca:
        lista = [m for m in lista_completa if busca in m.lower()]
    else:
        lista = lista_completa

    return render_template('home.html', person=person, musicas=lista, busca=busca, musica_editar=None)

