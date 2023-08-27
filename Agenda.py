# inclusão das bibliotecas 
from tkinter.ttk import*
from tkinter import*
from tkinter import messagebox

# Variaveis das cores

co0 = "#f0f3f5" # preto
co1 = "#f0f3f5" # cinza
co3 = "#38576b" # black

# Criação da janela
janela = Tk()
janela.title("")
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames

frame_cima = Frame(janela, width=500, height=50, bg=co3, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=500, height=150, bg=co1, relief="flat")

# 

nome = []
telefone = []

x = 0

def salvarContato():
    nome[x] = input("Digite um nome: \n")
    telefone[x] = input("Digite um telefone: \n")

