'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''

class bombaCombustivel():
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    def abastecerPorValor(self, valor):
        abastecimento = self.valorLitro * valor
        return abastecimento
    def abastecerPorLitro(self, litro):
        voltaValor = litro / self.valorLitro
        return voltaValor
    def alterarValor(self, valorNovo):
        self.valorLitro = valorNovo
    def alterarCombustivel(self, combustivelNovo):
        self.tipoCombustivel = combustivelNovo
    def alterarQuantidadeCombustivel(self, retirado):
        self.quantidadeCombustivel -= retirado

def menu():
    print("\n\n")
    print("Opções:")
    print("1. Abastecer")
    print("2. Alterar valor do combustivel")
    print("3. Alterar tipo do combustivel")
    print("4. Abastecer o posto (carro pipa)")

petrobras = bombaCombustivel("melhor", 6.30, 100)

while True:
    menu()
    acao = input("Digite o número da opção que deseja: ")
    if acao == '1':
        
    elif acao == '2':
    
    elif acao == '3':
    
    elif acao == '4':
    
    else:
        print("Ação invalida")