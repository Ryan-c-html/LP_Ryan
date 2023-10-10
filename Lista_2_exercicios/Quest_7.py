'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade 
Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, 
Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em consideração, 
o Humor do nosso tamagushi, este humor é uma combinação entre os 
atributos Fome e Saúde, ou seja, um campo calculado, então não 
devemos criar um atributo para armazenar esta informação por 
que ela pode ser calculada a qualquer momento.
'''
class bichinhoVirtual():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = float(fome)
        self.saude = float(saude)
        self.idade = int(idade)
    def alterarNome(self, nome):
        self.nome = nome
    def alimentar(self):
        if self.fome > 0:
            self.fome -= 10
    def curar(self):
        if self.saude < 100:
            self.saude += 10
    def envelhecer(self):
        self.idade += 1
    def informaNome(self):
        return self.nome
    def informaFome(self):
        return self.fome
    def informaSaude(self):
        return self.saude
    def informaIdade(self):
        return self.idade
    def informaHumor(self):
        if self.saude > 70:
            if self.fome < 20:
                return "O seu bichinho está de otimo humor"
            elif 20 < self.fome < 50:
                return "O seu bichinho está com o humor estavel, mas é recomendado que se alimente ele"
            else:
                return "O Seu bichinho está de pessimo humor"

pou = bichinhoVirtual("pou", 70, 100, 1)

print(f"\n\n\nO nome do seu bichinho é: {pou.informaNome()}")
print(pou.informaHumor())
print(f"\n{pou.informaFome()}")