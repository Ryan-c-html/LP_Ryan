'''

Classe Pessoa: Crie uma classe que modele uma pessoa:

1. Atributos: nome, idade, peso e altura
2. Métodos: Envelhercer, engordar, emagrecer, crescer. 
   Obs: Por padrão, a cada ano que passa nossa pessoa envelhece, 
   sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome   = nome
        self.idade  = int(idade)
        self.peso   = float(peso)
        self.altura = float(altura)
    def envelhecer(self):
        self.idade += 1
        if(self.idade < 21):
            self.altura = self.altura + 0.05
    def engordar(self):
        self.peso += 1
    def emagrecer(self):
        self.peso -= 1
    def crescer(self):
        self.altura += 1
    def printar(self, num):
        if(num == 1):return self.nome
        if(num == 2):return self.idade
        if(num == 3):return self.peso
        if(num == 4):return self.altura


ryan = pessoa( "Ryan", 17, 70, 1.73)
ryan.envelhecer()
num = input("\n\n\n\n\nO que você deseja saber sobre a pessoa? Pressione\n1 - Nome\n2 - Idade\n3 - Peso\n4 - Altura\n")
num = int(num)
print(f"O nome da pessoa é {ryan.printar(num)}")