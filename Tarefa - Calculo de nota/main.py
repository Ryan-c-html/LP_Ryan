# Inclusão das bibliotecas
from flask import Flask, render_template, request, redirect, url_for
# inclui a página criada ao programa principal e depois inclui suas funções
from modelo import Professor, Aluno
# inclui as bibliotecas usadas para abrir automaticamente o projeto
import webbrowser
import threading

app = Flask(__name__)


# Página de inicio (Main)
@app.route('/', methods=['POST', 'GET'])
def inicio():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        # Verifica se o botão apertado era o de login
        if botaoSelecionado == 'login':
            return redirect("/login")
        # Verifica se o botão apertado era o de tarefas
        if botaoSelecionado == 'tarefas':
            return redirect("/tarefas")
        # Verifica se o botão apertado era o de médias
        if botaoSelecionado == 'medias':
            return redirect("/medias")
    # exibe a tela inicial
    return render_template("main.html")

# Página de Login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # pega o nome inserido no campo de texto
        loginNome = request.form['nome']
        # pega a senha inserida no campo de texto
        loginSenha = request.form['senha']

        # define o objeto professor como global
        global professor1
        # cria o objeto professor
        professor1 = Professor(loginNome, loginSenha)
        # verifica se é um professor válido
        if professor1.verifica():
            return redirect("/redireciona")
        # se não for, reseta a página retornando a tela de login novamente
        else:
            return redirect("/login")
    # exibe a tela de login
    return render_template("login.html")

# Página de tarefas
@app.route('/tarefas', methods=['POST', 'GET'])
def tarefas():
    # pega o conteúdo de tarefa para exbir ao aluno
    conteudo = Aluno.leTarefa()
    return render_template("tarefas.html", conteudo=conteudo)

# Página de médias
@app.route("/medias", methods=['POST', 'GET'])
def medias():
    # pega o conteúdo de notas para exbir ao aluno
    conteudo = Aluno.leNota()
    return render_template("medias.html", conteudo=conteudo)

# Página de redirecionamento
@app.route("/redireciona", methods=['POST', 'GET'])
def redireciona():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        # se o botão for o da tarefa, chama a tela de tarefasProfessor
        if botaoSelecionado == 'tarefa':
            return redirect("/tarefasProfessor")
        # se o botão for o de notas, chama a tela de notasProfessor
        elif botaoSelecionado == 'notas': 
            return redirect("/notasProfessor")
        # se o botão for do tipo voltar retorna a tela de redirecionamento
        elif botaoSelecionado == 'voltar':
            return redirect("/")
    # exibe a tela de redirecionamento
    return render_template("redirecionaProfessor.html")

# Página de tarefas do professor
@app.route("/tarefasProfessor", methods=['POST', 'GET'])
def tarefaProfessor():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        # se o botão for o de criar tarefa e os campos estiverem preenchidos, cria a tarefa
        if botaoSelecionado == 'criaTarefa' and request.form['dataEntrega'] != "" and request.form['nomeAtividade'] != "":
            # pega a data inserida
            data = request.form['dataEntrega']
            # pega o nome da tarefa
            nomeTarefa = request.form['nomeAtividade']
            # pega a descrição da tarefa
            tarefa = request.form['tarefa']
            # cadastra a tarefa usando o objeto professor
            professor1.cadastroTarefa( data, nomeTarefa, tarefa)
        # se o botão for do tipo voltar retorna a tela de redirecionamento
        elif botaoSelecionado == 'voltar':
            return redirect("/redireciona")
    return render_template("tarefaProfessor.html")

# Página de notas
@app.route("/notasProfessor", methods=['POST', 'GET'])
def notaProfessor():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        # verifica se o botão de cadastrar nota foi apertado
        if botaoSelecionado == 'cadastraNota':
            # tenta postar a nota
            try:
                nome = request.form['nomeAluno']
                dre = request.form['dreAluno']
                aluno1 = Aluno(nome, dre)
                nota1 = request.form['nota1']
                nota2 = request.form['nota2']
                lista1 = request.form['lista1']
                lista2 = request.form['lista2']
                lista3 = request.form['lista3']
                lista4 = request.form['lista4']
                aluno1.postagemNotas(nota1, nota2, lista1, lista2, lista3, lista4)
            # em caso de erro reseta a página 
            except:
                return redirect("/notasProfessor")
        elif botaoSelecionado == 'voltar':
            return redirect("/redireciona")
    return render_template("notaProfessor.html")

# Função para iniciar o site
def inicia_site():
    app.run()

if __name__ == '__main__':
    # Inicia o site em uma thread separada
    threading.Thread(target=inicia_site).start()
    
    try:
        # Abre o navegador automaticamente na página local
        webbrowser.open("http://localhost:5000/")
    except Exception as e:
        print("Erro ao abrir o navegador: " + str(e))
