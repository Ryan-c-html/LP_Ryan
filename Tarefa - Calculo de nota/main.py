# Inclusão das bibliotecas
from flask import Flask, render_template, request, redirect, url_for
# inclui a página criada ao programa principal e depois inclui suas funções
from modelo import professor, aluno

app = Flask(__name__)

professor1 = professor()

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
    return render_template("redirecionaProfessor.html")

# Coloca o programa para rodar, tirar o "debug=True" qaundo o programa estiver finalizado
app.run(debug=True)
#app.run()