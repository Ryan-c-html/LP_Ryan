# Inclusão da biblioteca
from flask import Flask, render_template, request, redirect, url_for
from fpdf import FPDF

app = Flask(__name__)

# Página de main (Home)
@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        loginNome = request.form['Nome']
        loginSenha = request.form['Senha']
        #if verificarCredenciais(loginNome, loginSenha):
        #    return redirect("/pagina_dados")
        return redirect("/pagina_dados")
    return render_template('login.html')

#Pagina de cadastro
@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        cadastroNome = request.form['nome']
        cadastroSenha = request.form['senha']
        
        r = open("emailflask/UsuariosCadastrados/usuarios.txt", "a")
        r.write(f"\n{cadastroNome} - {cadastroSenha}")
        
        return redirect("/pagina_dados")
    
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
        
        #criaPDF(data, destinatario)

        return redirect("/")    

    return render_template('pagina_dados.html')

def criaPDF(data, destinatario):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=13)
    txt = open("{data}_{destinatario}.txt", "r")
    lendo = txt.readlines()
    for ler in lendo:
        pdf.cell(200, 10, ler)
    pdf.output(f"emailflask/cartas/Cartas_PDF/{data}-{destinatario}.pdf")
    pdf.close()

def verificarCredenciais(Vnome, Vsenha):
    try:
        usuarios = {}
        with open("emailflask/UsuariosCadastrados/usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                Rnome, Rsenha = linha.strip().split(" - ")
                usuarios[Rnome] = Rsenha
                if Rnome == Vnome and Rsenha == Vsenha:
                    return True
    except FileNotFoundError:
        print("O arquivo de usuários não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")    
    return False

# Essa função faz com que o programa rode
app.run(debug=True)