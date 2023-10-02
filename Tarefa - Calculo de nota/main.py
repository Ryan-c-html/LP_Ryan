# Inclusão das bibliotecas
from flask import Flask, render_template, request, redirect, url_for
# inclui a página criada ao programa principal e depois inclui suas funções
from modelo import professor, aluno

app = Flask(__name__)

professor1 = professor()
aluno1 = aluno()

# Página de inicio (Main)
@app.route('/', methods=['POST', 'GET'])
def inicio():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        if botaoSelecionado == 'login':
            return redirect("/login")
        if botaoSelecionado == 'tarefas':
            return redirect("/tarefas")
        if botaoSelecionado == 'medias':
            return redirect("/medias")
    return render_template("main.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        loginNome = request.form['nome']
        loginSenha = request.form['senha']
        if professor1.verifica(loginNome, loginSenha):
            return redirect("/redireciona")
        else:
            return redirect("/login")
    return render_template("login.html")

@app.route('/tarefas', methods=['POST', 'GET'])
def tarefas():
    return render_template("tarefas.html")

@app.route("/medias", methods=['POST', 'GET'])
def medias():
    return render_template("medias.html")

@app.route("/redireciona", methods=['POST', 'GET'])
def redireciona():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        if botaoSelecionado == 'tarefa':
            return redirect("/tarefasProfessor")
        elif botaoSelecionado == 'notas': 
            return redirect("/notasProfessor")
        elif botaoSelecionado == 'voltar':
            return redirect("/")
    return render_template("redirecionaProfessor.html")

@app.route("/tarefasProfessor", methods=['POST', 'GET'])
def tarefaProfessor():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        if botaoSelecionado == 'criaTarefa':
            data = request.form['dataEntrega']
            nomeTarefa = request.form['nomeAtividade']
            tarefa = request.form['tarefa']
            professor1.cadastroTarefa( data, nomeTarefa, tarefa)
        elif botaoSelecionado == 'voltar':
            return redirect("/redireciona")
    return render_template("tarefaProfessor.html")

@app.route("/notasProfessor", methods=['POST', 'GET'])
def notaProfessor():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        if botaoSelecionado == 'cadastraNota':
            nome = request.form['nomeAluno']
            dre = request.form['dreAluno']
            nota1 = request.form['nota1']
            nota2 = request.form['nota2']
            lista1 = request.form['lista1']
            lista2 = request.form['lista2']
            lista3 = request.form['lista3']
            lista4 = request.form['lista4']
            aluno1.postagemNotas(nome, dre, nota1, nota2, lista1, lista2, lista3, lista4)
        elif botaoSelecionado == 'voltar':
            return redirect("/redireciona")
    return render_template("notaProfessor.html")

# Coloca o programa para rodar, tirar o "debug=True" qaundo o programa estiver finalizado
app.run(debug=True)
#app.run()