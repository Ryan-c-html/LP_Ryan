'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador 
para controlar o rendimento diário de seu trabalho. Toda vez que 
ele traz um peso de peixes maior que o estabelecido pelo regulamento 
de pesca do estado de São Paulo (50 quilos) deve pagar uma multa 
de R$ 4,00 por quilo excedente. João precisa que você faça um 
programa que leia a variável peso (peso de peixes) e calcule 
o excesso. Gravar na variável excesso a quantidade de quilos 
além do limite e na variável multa o valor da multa que João 
deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

multa = 4.00

print("Olá, João")

peso = input("\nQual é o peso de todos os peixes que foram pescados?\nOBS: Coloque o peso dos peixes em gramas\n")
peso = float(peso)

if(0 < peso <= 50000):
    pesoPeixe = float(peso / 1000)
    print(f"Os peixes pesam: {pesoPeixe}\nNão possui peso em excesso e portanto não possui multa")
elif(peso > 50000):
    pesoPeixe = float(peso / 1000)
    excesso = (pesoPeixe - 50)
    multa   = float(excesso * multa)
    print(f"Peso: {pesoPeixe}\nExcesso: {excesso}\nMulta: R$ {multa}")
else:
    print("O valor de peso é invalido")