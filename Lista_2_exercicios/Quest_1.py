'''
Classe Bola: Crie uma classe que modele uma bola:
1. Atributos: Cor, circunferência, material
1. Métodos: trocaCor e mostraCor
'''

# Criando uma classe bola
class Bola():
    # A primeira função irá receber as variaveis que serão usadas em toda a classe
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    # Metodo que irá trocar a cor da bola
    def trocaCor(self, cor):
        self.cor = cor

    # Metodo que irá mostrar a cor da bola
    def mostraCor(self):
        return f"A cor da bola é: {self.cor}"

# Definindo uma instancia bola1 que será associada a classe Bola
bola1 = Bola("verde", 30, "metal")

# printa a cor da Bola
print(bola1.mostraCor())

# Pede uma nova cor para a bola
novaCor = input("Qual é a cor dessejada para a bola?")

# Troca a cor da Bola a partir da nova Cor
bola1.trocaCor(novaCor)

# Printa a cor atual da bola
print(bola1.mostraCor())