# Codigo de uma lista telefonica
x = 0

nome = []
telefone = []

def novoContato():
    nome[x] = input("Digite um nome: \n")
    telefone[x] = input("Digite um telefone: \n")
    x = x + 1

def editarContato():
    a = input("Qual contato você deseja editar? \n")
    print("Você deseja editar o contato do(a) " + nome[a] + "?\n")
    l = input("Se sim escreva 's', e se não escreva 'n'")
    
    print()

def removerContato():
    pass

def verContato():
    pass

def Terminar():
    
    pass

