'''
Aprimore a classe do exercício anterior 
para adicionar o método aumentarSalario 
(porcentualDeAumento) que aumente o salário 
do funcionário em uma certa porcentagem.
'''
class funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)
    def devolveNome(self):
        print(f"O nome do funcionario é: {self.nome}")
    def devolveSalario(self):
        print(f"O salario do seu funcionario é: {self.salario}")

class aumentaSalario(funcionario):
    def aumentarSalario(self, valor):
        aumento = self.salario * (valor / 100)
        self.salario += aumento

Ryan = aumentaSalario("Ryan", 1200)

Ryan.devolveNome()
Ryan.devolveSalario()
print("\n")
Ryan.aumentarSalario(50)
Ryan.devolveSalario()