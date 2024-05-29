from app import app
from flask import render_template
from flask import request
import json
import requests
link = "https://ti18n-f62da-default-rtdb.firebaseio.com/" #conecta o banco de dados

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo='Pagina Inicial', nome='Fernanda')

@app.route('/contato')
def contato():
    return render_template('/contato.html', titulo='Contato', nome='Fernanda')

@app.route('/colecoes')
def colecoes():
    return render_template('colecoes.html', titulo="Coleções", nome="Fernanda")

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo="Sobre", nome="Fernanda")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastro", nome="Fernanda")

@app.route('/parceiros')
def parceiros():
    return render_template('parceiros.html', titulo="Parceiros", nome="Fernanda")

@app.route('/registrar')
def registrar():
    return render_template('registrar.html', titulo="Registrar", nome="Fernanda")

@app.route('/login')
def login():
    return render_template('login.html', titulo="Login", nome="Fernanda")

@app.route('/administrador')
def administrador():
    return render_template('administrador.html', titulo="Acesso Administrador", nome="Fernanda")

@app.route('/usuario')
def usuario():
    return render_template('usuario.html', titulo="Acesso Usuário", nome="Fernanda")
#metodos para manipulacao dos dados

#cadastro
@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        nome     = request.form.get("txtNome")
        email    = request.form.get("txtMail")
        telefone = request.form.get("txtTel")
        senha    = request.form.get("txtSenha")
        dados = {"nome":nome, "email":email, "telefone":telefone, "senha":senha}
        requisicao = requests.post(f'{link}/cadastrar/.json', data=json.dumps(dados))
        return 'Cadastrado com Sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

#login
@app.route('/logar', methods=['POST'])
def entrar():
    email = request.form.get("txtLoginMail")
    senha = request.form.get("txtLoginSenha")
    requisicao = requests.get(f'{link}/cadastrar/.json')  # solicitar os dados
    dicionario = requisicao.json()
    usuario = ''
    try:
            for codigo in dicionario:
                usuario = dicionario[codigo]['email']
                sen     = dicionario[codigo]['senha']
                if (usuario == email and sen == senha):
                    return usuario

            return 'erro'
    except Exception as e:
            return f'Ocorreu um erro\n\n {e}'


@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json')#solicitar os dados
        dicionario = requisicao.json()
        return dicionario
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/listarIndividual')
def listarIndividual():
    requisicao = requests.get(f'{link}/cadastrar/.json')
    dicionario = requisicao.json()
    idCadastro = ""
    try:
        for codigo in dicionario:
                usuario = dicionario[codigo]['nome']
                if(usuario == 'teste'):
                    idCadastro = codigo
                return idCadastro
    except Exception as e:
            return f'Algo deu errado!\n\n + {e}'

    # -NySO_S4fUqHm7Esx0zn

@app.route('/atualizar')
def atualizar():
    try:
        dados = {"email":"fefe@gmail.com"}#parametro para atualizaçao
        requisicao = requests.patch(f'{link}/cadastrar/-NySO_S4fUqHm7Esx0zn/.json', data=json.dumps(dados))
        return"Atualizado com sucesso!"
    except Exception as e:
        return f'Houve um erro!\n\n + {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao =requests.delete(f'{link}/cadastrar/-NySO_S4fUqHm7Esx0zn/.json')
        return "Excluido com sucesso!"
    except Exception as e:
        return f'Houve um erro!\n\n + {e}'