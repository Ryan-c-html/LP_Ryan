# inclusão das bibliotecas 
from tkinter.ttk import*
from tkinter import*
from tkinter import messagebox

# Variaveis das cores

co0 = "#f0f3f5" # preto
co1 = "#f0f3f5" # cinza

# Criação da janela
janela = Tk()
janela.title("Agenda")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

nome = []
telefone = []

x = 0

def salvarContato():
    nome[x] = input("Digite um nome: \n")
    telefone[x] = input("Digite um telefone: \n")

