# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de
# informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível
# do volume permanecem dentro de faixas válidas.

class TV:

    def __init__(self):
        self.volume = 0
        self.canal = 1
        self.ligado = 'OFF'

    def Volume(self, v):

        if v == '+':
            if self.volume == 60:
                print('Volume Máximo\n')
            else:
                self.volume += 1


        elif v == '-':
            if self.volume == 0:
                print('Volume Mínimo\n')
            else:
                self.volume -= 1

        else:
            print('Valor inválido\n')

    def Canal(self, n):

        if 0 < n < 100:
            self.canal = n


        else:
            print('Os canais vão de 1 à 100\n')

    def Ligar(self):

        if self.ligado == 'ON':
            self.ligado = 'OFF'

        else:
            self.ligado = 'ON'


tv = TV()


while True:

    try:

        print(f' {tv.ligado}         Volume  {tv.volume}          Canal  {tv.canal}  \n')
        a = input('(+,-) Volume\n (número) Canal\n (l) Liga/Desliga\n\n\n\n\n')

        if a == '+':
            tv.Volume(a)

        elif a == '-':
            tv.Volume(a)

        elif a == 'l':
            tv.Ligar()

        else:
            a = int(a)
            tv.Canal(a)


    except:
        pass
