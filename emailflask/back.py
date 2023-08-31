from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

# Página de login
@app.route('/')
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
            f.write(f"Data: {data}\nDestinatário: {destinatario}\nMensagem: {mensagem}\nRemetente: {remetente}")

    return render_template('pagina_dados.html')

if _name_ == '_main_':
    app.run(debug=True)