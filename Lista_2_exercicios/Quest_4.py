'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

1. Atributos: nome, idade, peso e altura
2. Métodos: Envelhercer, engordar, emagrecer, crescer. 
   Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
   sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome   = nome
        self.idade  = idade
        self.peso   = peso
        self.altura = altura
    def envelhecer(self):
        self.idade += 1
    def engordar(self):
        self.peso += 1
    def emagrecer(self):
        self.peso -= 1
    def crescer(self):
        self.altura += 1