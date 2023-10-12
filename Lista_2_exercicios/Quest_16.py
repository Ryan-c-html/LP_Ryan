'''
Crie uma "porta escondida" no programa 
do programa do bichinho virtual que mostre 
os valores exatos dos atributos do objeto. 
Consiga isto mostrando o objeto quando uma 
opção secreta, não listada no menu, for informada 
na escolha do usuário. Dica: acrescente um método 
especial str() à classe Bichinho.
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
    def __str__(self):
        return f"Informações do Pou:\nNome: {self.nome}\nIdade: {self.idade}\nSaude: {self.saude}\nFome: {self.fome}\nHumor: {self.humor}"

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
    elif acao == '10':
        mensagem = str(pou)
        print(mensagem)
    else:
        print("\nAção invalida")
    input("")
    niveis()