'''
11)Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1. O produto do dobro do primeiro com metade do segundo.
2. A soma do triplo do primeiro com o terceiro.
3. O terceiro elevado ao cubo.
'''
n = 0
n1 = int(input("Digite um número interiro:  "))
n2 = int(input("Digite um número inteiro: "))
n3 = float(input("Digite um número real: "))

n = int((2*n1)*(n2/2))

print(f"O produto do dobro do primeiro com metade do segundo é: {n}")

n = ((3*n1) + (n3))

print(f"A soma do triplo do primeiro com o terceiro é: {n}")

n = (n3*n3*n3)

print(f"O terceiro elevado ao cubo é: {n}")