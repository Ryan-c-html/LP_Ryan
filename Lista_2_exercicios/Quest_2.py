'''
Classe Quadrado: Crie uma classe que modele um quadrado:

1. Atributos: Tamanho do lado
2. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado():
    def __init__(self, lado):
        self.lado = float(lado)

    def mudarLado(self, novoLado):
        self.lado = novoLado
    def retornaLado(self):
        return self.lado
    def area(self):
        return (self.lado * self.lado)

quad1 = Quadrado(10)

print(f"O lado do quadrado é: {quad1.retornaLado()}\n")

novoLado = input("Qual é o novo lado para o quadro? \n")
novoLado = float(novoLado)
quad1.mudarLado(novoLado)

print(f"O novo lado do quadrado é: {quad1.retornaLado()}\n")

print(f"A area do quadrado é: {quad1.area()}")