# Codigo de uma lista telefonica
x = 0

nome = []
telefone = []

def novoContato():
    nome[x] = input("Digite um nome: ")
    telefone[x] = input("Digite um telefone: ")
    x = x + 1
    pass

def editarContato():
    a = input("Qual contato você deseja editar? \n")
    print("Você deseja editar o contato do(a) " + nome[a] + "?")
    a = input()
    print()
    pass

def removerContato():
    pass

def verContato():
    pass

def Terminar():
    
    pass

