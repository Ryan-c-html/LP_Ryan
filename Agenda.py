# inclusão das bibliotecas 
from tkinter.ttk import*
from tkinter import*
from tkinter import messagebox



nome = []
telefone = []

x = 0

def salvarContato():
    nome[x] = input("Digite um nome: \n")
    telefone[x] = input("Digite um telefone: \n")

