'''
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
'''

class ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def imprimeValores(self):
        print(f"x: {self.x}e y: {self.y}")

class retangulo():
    def __init__(self, pontoInicial, largura, altura):
        self.pontoinicial = pontoInicial
        self.largura = largura
        self.altura = altura
    def centro(self):
        centroLargura = (self.pontoinicial.x + self.largura) / 2
        centroAltura = (self.pontoIncial.y + self.altura) / 2
        return ponto(centroAltura, centroLargura)

def menu():
    print("\n\n\n")
    print("1. Criar retangulo")
    print("2. Encontrar centro\n")

print("\n\n\nComeço do programa!")

quadrado = None
while True:
    menu()
    opcao = input("Deseja qual das opções?")
    if opcao == '1':
        x = float(input("O (x) onde o triangulo começa: "))
        y = float(input("O (y) onde o triangulo começa: "))
        lado1 = float(input("O primeiro lado do retangulo é: "))
        lado2 = float(input("O segundo lado do retangulo é: "))
        pontoInicial = ponto(x, y)
        quadrado = retangulo(pontoInicial, lado1, lado2)
    elif opcao == '2':
        if quadrado:
            centro = quadrado.centro()
            print(f"O centro do objeto é: {centro}")
        else:
            print("Ação invalida. Crie o retangulo primeiro")
    else:
        print("Opção invalida!")
