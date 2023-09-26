'''
Classe Retangulo: Crie uma classe que modele um retangulo:

1. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
2. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
3. Crie um programa que utilize esta classe. 
   Ele deve pedir ao usuário que informe as medidades de um local. 
   Depois, deve criar um objeto com as medidas e calcular a quantidade de 
   pisos e de rodapés necessárias para o local

OBS: Levei em consideração que o piso tem 0,5 m²
'''

class retangulo():
    def __init__(self, ladoA, ladoB):
        self.ladoA = float(ladoA)
        self.ladoB = float(ladoB)
    def mudarValores(self, novoLadoA, novoLadoB):
        self.ladoA = novoLadoA
        self.ladoB = novoLadoB
    def retornavalores(self):
        return 
    def calculaArea(self):
        return (self.ladoA * self.ladoB)
    def calculaPerimetro(self):
        return ((self.ladoA * 2) + (self.ladoB * 2))

print("\n\n\n\n______Bem Vindo !______\n\n")
print("- - Informe os valores dos lados do retangulo - -")

novoLadoA = float(input("Informe o primeiro lado: "))
novoLadoB = float(input("Informe o segundo lado: "))

retang1 = retangulo(novoLadoA, novoLadoB)

print(f"Area do retangulo: {retang1.calculaArea()} m²\n")
pisos = (retang1.calculaArea() * 2)
print(f"\n\nA quantidade de pisos necessarios é: {pisos}")