'''
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
'''

print("Qual é a sua altura?")
altura    = float(input("OBS: Informe o valor em centimetros "))
altura = altura / 100
pesoIdeal = float(((72.7 * altura) - 58)) 

if(0.40 < altura < 2.50):
    pesoIdeal = float(((72.7 * altura) - 58))
    print(f"O seu peso ideal é {pesoIdeal}")
else:
    print("Altura invalida")