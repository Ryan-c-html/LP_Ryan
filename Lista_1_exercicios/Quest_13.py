'''
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:

Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

genero = input("Digite:\n'h' se for um homem\n'm' se for uma mulher\nOBS: Os dois precisam ser minusculos.\n")

print("Qual é a sua altura?")
altura = float(input("OBS: Informe o valor em centimetros\n"))
altura = altura / 100
if(genero == 'h'):
    if(0.40 < altura < 2.50):
        pesoIdeal = float(((72.7 * altura) - 58))
        print(f"O seu peso ideal é {pesoIdeal}")
    else:
        print("Altura invalida")
elif(genero == 'm'):
    if(0.40 < altura < 2.50):
        pesoIdeal = float(((62.1*altura) - 44.7))
        print(f"O seu peso ideal é {pesoIdeal}")
    else:
        print("Altura invalida")
else:
    if(0.40 < altura < 2.50):
        print("A resposta para genero foi invalida")
    else:
        print("A resposta para genero e para altura é invalida")
