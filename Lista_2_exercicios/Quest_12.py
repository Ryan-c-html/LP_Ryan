'''
Classe Conta de Investimento: Faça uma classe 
contaInvestimento que seja semelhante a classe 
contaBancaria, com a diferença de que se adicione 
um atributo taxaJuros. Forneça um construtor que 
configure tanto o saldo inicial como a taxa de juros. 
Forneça um método adicioneJuros (sem parâmetro explícito) 
que adicione juros à conta. Escreva um programa que 
construa uma poupança com um saldo inicial de R$1000,00 
e uma taxa de juros de 10%. Depois aplique o método 
adicioneJuros() cinco vezes e imprime o saldo resultante.
'''
class contaInvestimento():
    def __init__(self, numConta, nomeCorrentista, saldoInicial, taxaJuros):
        self.numConta = float(numConta)
        self.nomeCorrentista = nomeCorrentista
        self.saldo = float(saldoInicial)
        self.taxaJuros = float(taxaJuros)
    def alterarNome(self, nome):
        self.nomeCorrentista = nome
    def deposito(self, dinheiro):
        self.saldo += dinheiro
    def saque(self, dinheiro):
        self.saldo -= dinheiro
    def verificarSaldo(self):
        return self.saldo
    def adicionaJuros(self):
        juros = (self.saldo) * (self.taxaJuros / 100)
        self.saldo += juros

contaRyan = contaInvestimento(1234, "Ryan", 1000, 10)

contaRyan.adicionaJuros()
contaRyan.adicionaJuros()
contaRyan.adicionaJuros()
contaRyan.adicionaJuros()
contaRyan.adicionaJuros()

print(f"O saldo resultante é: {contaRyan.verificarSaldo()}")