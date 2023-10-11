'''

Classe Conta Corrente: Crie uma classe para implementar uma conta corrente:

1. Atributos: número da conta, nome do correntista e saldo. 
2. Métodos: alterarNome, depósito e saque; 
    No construtor, saldo é opcional, com valor default zero e os 
    demais atributos são obrigatórios.
'''

class contaCorrente():
    def __init__(self, numConta, nomeCorrentista, saldo):
        self.numConta = float(numConta)
        self.nomeCorrentista = nomeCorrentista
        self.saldo = float(saldo)
    def alterarNome(self, nome):
        self.nomeCorrentista = nome
    def deposito(self, dinheiro):
        self.saldo += dinheiro
    def saque(self, dinheiro):
        self.saldo -= dinheiro
    def verificarSaldo(self):
        return self.saldo

conta1 = contaCorrente(1055, "Ryan", 10000)

print("\n\n\n\n_____Bem vindo ao nosso banco!_____\n")

while True:
    print("Ações:\n         1. Acessar saldo\n         2. Depositar\n         3. Sacar\n         4. Alterar Nome\n")
    acao = input("Qual será sua primeira ação?")
    if(acao == '1'):
        print(f"\nO seu saldo é: {conta1.verificarSaldo()}")
    elif(acao == '2'):
        dinheiro = float(input("\nO quanto deseja depositar?\n"))
        conta1.deposito(dinheiro)
        print(f"\nVocê possui {conta1.verificarSaldo()} na sua conta")
    elif(acao == '3'):
        dinheiro = float(input("\nO quanto deseja sacar?\n"))
        conta1.saque(dinheiro)
        print(f"\nVocê possui {conta1.verificarSaldo()} na sua conta")
    elif(acao == '4'):
        nome = input("\nQual será seu novo nome?")
        conta1.alterarNome(nome)
        print(f"Seu nome foi alterado para {conta1.nomeCorrentista}")
    else:
        print("\n\nAção invalida")