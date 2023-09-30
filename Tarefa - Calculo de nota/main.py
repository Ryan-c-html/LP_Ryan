# Inclusão das bibliotecas
from flask import Flask, render_template, request, redirect, url_for
from fpdf import FPDF

app = Flask(__name__)

# Página de inicio (Main)
@app.route('/', methods=['POST', 'GET'])
def inicio():
    if request.method == 'POST':
        botaoSelecionado = request.form['botao']
        if botaoSelecionado == 'login':
            return redirect("/login")
        if botaoSelecionado == '':
            return redirect("/tarefas")
    return render_template("main.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route('/tarefas', methods=['POST', 'GET'])
def tarefas():
    return render_template("tarefas.html")

# Coloca o programa para rodar, tirar o "debug=True" qaundo o programa estiver finalizado
app.run(debug=True)
#app.run()