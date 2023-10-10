'''
Classe Macaco: Desenvolva uma classe Macaco,que possua os 
atributos nome e bucho (estomago) e pelo menos os 
métodos comer(), verBucho() e digerir(). 
Faça um programa ou teste interativamente, 
criando pelo menos dois macacos, alimentando-os com 
pelo menos 3 alimentos diferentes e verificando o conteúdo
do estomago a cada refeição. Experimente fazer com que um 
macaco coma o outro. É possível criar um macaco canibal?
'''

class macaco():
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho
    def comer(self, comida):
        self.bucho = self.bucho + comida
    def verBucho(self):
        return f"{self.bucho}"
        #return self.bucho
    def digerir(self):
        self.bucho = 0

mico = macaco("mico", "comida")
gorila = macaco("gorila", "maçã")
orangotango = macaco("oragotango", "banana")

#print(f"No bucho do gorila tem: {gorila.verBucho()}")
print(f"No bucho do gorila tem: ", gorila.verBucho())
comida = ", "
comida += input("Deseja alimentar o gorila com? ")
gorila.comer(comida)

comidas = {", banana",", morango",", chocolate"}
for i in comidas:
    gorila.comer(i)
    mico.comer(i)
    orangotango.comer(i)

print("\n", gorila.verBucho())

#Tentei a função do macaco canibal, mas ela não funcionou