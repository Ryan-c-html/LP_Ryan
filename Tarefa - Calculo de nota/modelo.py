# A página de modelo terá algumas classes e funções

# Importando as bibliotecas necessarias
from fpdf import FPDF
from time import sleep

class professor():
    def __init__(self):
        pass
    def verifica(self, nome, senha):
        self.nome = nome 
        self.senha = senha
        with open("/logins.txt", "r") as txt:
            linhas = txt.readlines()
            for linha in linhas:
                linha = linha.strip("\n")
                dados = linha.append(linha.split("-"))
            for i in dados:
                if self.nome == i[0] and self.senha == i[1]:
                    return True
    def cadastro(self, nome, senha):
        self.nome = nome
        self.senha = senha
        with open("./logins.txt", "a") as txt:
            txt.write(f"{self.nome} - {self.senha}\n")