# Inclusão da biblioteca
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página de main (Home)
@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        name = request.form.get("botao")
        if name == 'logar':
            return redirect ("/login")
        elif name == 'cadastrar':
            return redirect ("/cadastro")
    return render_template('main.html')

# Pagina de login
@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')

#Pagina de cadastro
@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome  = request.form['nome']
        cpf   = request.form['cpf']
        senha = request.form['senha']
    
    return render_template('cadastro.html')

# Essa pagina vai receber a carta e suas variaveis e após isso vai criar a carta em txt
@app.route('/pagina_dados', methods=['POST', 'GET'])
def pagina_dados():
    if request.method == 'POST':
        data = request.form['data']
        destinatario = request.form['destinatario']
        mensagem = request.form['mensagem']
        remetente = request.form['remetente']

        f = open(f'{data}_{destinatario}.txt', 'w')
        f.write(f"Data: {data}\nDestinatario: {destinatario}\nMensagem: {mensagem}\nRemetente: {remetente}")
        
        return redirect("/login")

    return render_template('pagina_dados.html')

# Essa função faz com que o programa rode
app.run()