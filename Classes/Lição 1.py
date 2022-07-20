#Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self,cor,raio,material):
        self.cor = cor
        self.raio = raio
        self.material = material
        self.area = 4*3.14*(self.raio**2)
        self.volume = (4/3)*3.14*self.raio**3

    def trocaCor(self,cor):
        self.cor = cor
        print(f'Cor alterada para {self.cor}\n')

    def mostraCor(self):
        print(self.cor, '\n')

    def trocaRaio(self,raio):

        self.raio = raio
        print(f'Raio {self.raio}\nÁrea {self.area}\nVolume {self.volume}\n')

    def mostraGeometria(self):
        print(f'Raio {self.raio}\nÁrea {self.area}\nVolume {self.volume}\n')




bola_1 = Bola('Amarela',3,'Plástico')


while True:

    a = input('(1) Troca Cor\n(2) Mostra Cor\n(3) Troca Raio\n(4) Mostra Geometria\n ')
    print()

    if a == '1':

        cor = input('Cor desejada: ')
        bola_1.trocaCor(cor)

    elif a == '2':

        bola_1.mostraCor()

    elif a =='3':
        raio = float(input('Novo Raio: '))
        bola_1.trocaRaio(raio)

    elif a == '4':
        bola_1.mostraGeometria()

    else:
        print('Comando Inválido.\n')
