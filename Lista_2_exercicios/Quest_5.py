'''

Classe Conta Corrente: Crie uma classe para implementar uma conta corrente:

1. Atributos: número da conta, nome do correntista e saldo. 
2. Métodos: alterarNome, depósito e saque; 
    No construtor, saldo é opcional, com valor default zero e os 
    demais atributos são obrigatórios.
'''

class contaCorrente():
    def __init__(self, numConta, nomeCorrentista, saldo):
        self.numConta = numConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo
    def alterarNome(self, nome):
        self.nomeCorrentista = nome
    def deposito(self, dinheiro):
        self.saldo += dinheiro
    def saque(self, dinheiro):
        self.saldo -= dinheiro

