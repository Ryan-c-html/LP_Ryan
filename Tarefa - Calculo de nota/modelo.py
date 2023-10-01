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
        try:
            with open("./Tarefa - Calculo de nota/logins.txt", "r") as txt:
                linhas = txt.readlines()
                for linha in linhas:
                    linha = linha.strip()
                    dados = linha.split("-")
                    if len(dados) == 2 and self.nome == dados[0] and self.senha == dados[1]:
                        return True
        # Caso ocorra um erro ao encontrar o arquivo, as coisas que estão dentro dessa função começam a ser executadas
        except FileNotFoundError:
            # Essa parte cria um arquivo de login, caso o arquivo de login não existisse. Isso previne que ocorra erros 
            # atrapalhem o programa.
            with open("logins.txt", "w") as arquivo:
                arquivo.write("Miceli-1234\nRyan-1234")
            print("O arquivo 'logins.txt' não foi encontrado.")
        return False
    def cadastro(self, nome, senha):
        self.nome = nome
        self.senha = senha
        try: 
            with open("./Tarefa - Calculo de nota/logins.txt", "a") as txt:
                txt.write(f"{self.nome} - {self.senha}\n")
        except FileNotFoundError:
            with open("./Tarefa - Calculo de nota/logins.txt", "w") as txt:
                txt.write(f"{self.nome} - {self.senha}\n")
    def cadastroTarefa(self, data, nomeTarefa, tarefa):
        self.data = data
        self.nomeTarefa = nomeTarefa
        self.tarefa = tarefa
        with open(f"./Tarefa - Calculo de nota/Tarefas/{nomeTarefa}.txt", "w") as txt:
            txt.write(f"{self.nomeTarefa}\n{self.data}\n{self.tarefa}")

class aluno():
    def __init__(self):
        pass
    def calculaSituacao(self, t1, t2, l1, l2, l3, l4):
        media = (((t1 + t2) * 0.8) + (((l1 + l2 + l3 + l4) / 4)*0.2))
        if media >= 7:
            situação = "aprovado"
        elif 7 > media and media >= 3:
            situação = "final"
        else:
            situação = "reprovado"
        return situação