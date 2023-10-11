'''
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

- Um veículo tem um certo consumo de combustível (medidos em km / litro) e 
uma certa quantidade de combustível no tanque.
- O consumo é especificado no construtor e o nível de combustível inicial é 0.
- Forneça um método andar( ) que simule o ato de dirigir o veículo por uma 
certa distância, reduzindo o nível de combustível no tanque de gasolina.
- Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
- Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
'''
class carro():
    def __init__(self, kml):
        self.kml = float(kml)
        self.gasolina = 0
    def adicionarGasolina(self, gasolina):
        self.gasolina += gasolina
    def andar(self, km):
        self.gasolina = self.gasolina - km / self.kml 
    def obterGasolina(self):
        #return self.gasolina
        print(f"O tanque ainda possui {self.gasolina} de gasolina")

meuFusca = carro(30);          
meuFusca.adicionarGasolina(30);  
meuFusca.obterGasolina()
meuFusca.andar(30);           
meuFusca.obterGasolina()     