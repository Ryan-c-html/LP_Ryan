from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página de login
@app.route('/main', methods['GET'])
def main():
    if request.method == 'POST':
        name = request.form.get("botao")
        if name == 'logar':
            render_template('login.html')
        elif name == 'cadastro':
            render_template('cadastro.html')
    return render_template('main.html')

@app.route('/login', methods=['gets'])
def login():
    return render_template('login.html')

# Página após o login
@app.route('/pagina_dados', methods=['GET', 'POST'])
def pagina_dados():
    if request.method == 'POST':
        data = request.form['data']
        destinatario = request.form['destinatario']
        mensagem = request.form['mensagem']
        remetente = request.form['remetente']

        filename = f"{data}_{destinatario}.txt"
        with open(filename, 'w') as f:
            f.write(f"Data: {data}\nDestinatario: {destinatario}\nMensagem: {mensagem}\nRemetente: {remetente}")

    return render_template('pagina_dados.html')

@app.route('/cadastro', methods=['POST', 'POST'])
def cadastro():
        return render_template('cadastro.html')

app.run()