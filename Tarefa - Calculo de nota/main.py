# Inclusão das bibliotecas
from flask import Flask, render_template, request, redirect, url_for
from fpdf import FPDF

app = Flask(__name__)

# Página de inicio (Main)
@app.route('/', methods=['POST', 'GET'])
def inicio():
    return render_template("main.html")

# Coloca o programa para rodar, tirar o "debug=True" qaundo o programa estiver finalizado
app.run(debug=True)
#app.run()