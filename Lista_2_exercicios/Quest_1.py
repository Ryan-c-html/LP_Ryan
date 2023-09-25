'''
Classe Bola: Crie uma classe que modele uma bola:
1. Atributos: Cor, circunferência, material
1. Métodos: trocaCor e mostraCor
'''

#Criando uma classe bola
class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return f"A cor da bola é: {self.cor}"

bola1 = Bola("verde", 30, "metal")

print(bola1.mostraCor())

novaCor = input("Qual é a cor dessejada para a bola?")

bola1.trocaCor(novaCor)

print(bola1.mostraCor())