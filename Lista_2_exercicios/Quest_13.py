'''
Classe Funcionário: Implemente a classe Funcionário. 
Um empregado tem um nome (um string) e um salário(um double). 
Escreva um construtor com dois parâmetros (nome e salário) e 
métodos para devolver nome e salário. Escreva um pequeno 
programa que teste sua classe.
'''
class funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)
    def devolveNome(self):
        print(f"O nome do funcionario é: {self.nome}")
    def devolveSalario(self):
        print(f"O salario do seu funcionario é: {self.salario}")

Ryan = funcionario("Ryan", 1200)

Ryan.devolveNome()
Ryan.devolveSalario()