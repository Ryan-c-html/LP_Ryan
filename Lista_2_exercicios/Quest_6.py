'''
Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar
ou diminuir o volume. Certifique-se de que o número do canal e o 
nível do volume permanecem dentro de faixas válidas.
'''
volumeInicial = int(50)
volumeMaximo = int(100)
volumeMinimo = int(0)
class televisor():
    def __init__(self, canal, volume):
        self.canal = float(canal)
        self.volume = int(volume)
    def aumentarVolume(self):
        if(self.volume + 10 <= volumeMaximo):
            self.volume += 10
    def diminuirVolume(self):
        if(self.volume - 10 >= volumeMinimo):
            self.volume -= 10
    def volume(self):
        return f"O volume da televisão está em: {self.volume}%"

print("\n\n\n")

visor1 = televisor(4, volumeInicial)

print(f"Volume da tv: {visor1.volume}%")

visor1.aumentarVolume()

print(f"Volume da tv: {visor1.volume}%")

visor1.diminuirVolume()

print(f"Volume da tv: {visor1.volume}%\n")