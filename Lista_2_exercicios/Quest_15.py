'''
Classe Bichinho Virtual++: Melhore o programa 
do bichinho virtual, permitindo que o usuário 
especifique quanto de comida ele fornece ao 
bichinho e por quanto tempo ele brinca com o 
bichinho. Faça com que estes valores afetem 
quão rapidamente os níveis de fome e tédio caem.
'''
class bichinhoVirtual():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = float(fome)
        self.saude = float(saude)
        self.idade = int(idade)
        self.humor = 50
    def alterarNome(self, nome):
        self.nome = nome
    def alimentar(self, alimento): #O alimento será dado em porcentagem
        self.fome = self.fome - alimento
        if self.fome < 0:
            self.fome = 0
    def curar(self):
        if self.saude < 100:
            self.saude += 10
    def envelhecer(self):
        self.idade += 1
    def brincar(self, brincar): #O tempo de brincadeira vai ser em minutos
        self.humor += 50 * (brincar / 60)
        if self.humor > 100:
            self.humor = 100
    def informaNome(self):
        return self.nome
    def informaFome(self):
        return self.fome
    def informaSaude(self):
        return self.saude
    def informaIdade(self):
        return self.idade
    def informaHumor(self):
        return self.humor
    def escreveHumor(self):
        print(f"Seu bichinho está com {self.humor}%")
        if self.humor <= 40:
            print("Melhore o humor dele!")
        elif 40 < self.humor <= 60:
            print("O seu bichinho pode ficar mais feliz se você brincar com ele")
        elif 60 < self.humor:
            print("O humor do seu bichinho está otimo!")

pou = bichinhoVirtual("pou", 70, 100, 1)

def menu():
    print("\n")
    print("Opções:")
    print("   1. Alimentar")
    print("   2. Curar")
    print("   3. Brincar")
    print("   4. Envelhecer")

def niveis():
    multiplica = pou.informaHumor() / 100
    multiplica = multiplica * 10
    pou.fome += multiplica
    pou.saude -= multiplica

while True:
    menu()
    acao = input("Qual será sua ação? ")
    if acao == '1':
        print("Deseja alimentar o seu bichinho com quanto de comida?")
        quantidade = float(input("Quantidade (%): "))
        pou.alimentar(quantidade)
        print(f"A fome do seu {pou.informaNome()} está em: {pou.informaFome()} %")
    elif acao == '2':
        pou.curar()
        print(f"A saude do seu {pou.informaNome()} está em: {pou.informaSaude()} %")
    elif acao == '3':
        print("deseja brincar com o seu bichinho por quanto tempo?")
        tempo = float(input("Tempo (minutos): "))
        pou.brincar(tempo)
        print(f"O humor do seu {pou.informaNome()} está em: {pou.informaHumor()} %")
    elif acao == '4':
        print("O seu bichinho não está mais nessa idade?\nVou envelhecer o seu bichinho agora...")
        pou.envelhecer()
        print(f"A idade do seu {pou.informaNome()} é de: {pou.informaIdade()} Anos")
    else:
        print("\nAção invalida")
    input("")
    niveis()