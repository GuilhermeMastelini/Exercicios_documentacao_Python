#Classe Retangulo: Crie uma classe que modele um retangulo:
#
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

import math

class Piso:
    def __init__ (self,altura,largura):
        self.largura = largura
        self.altura = altura

    def Area(self):
        a = self.altura*self.largura
        a = '{:.2f}'.format(a)
        print(a,'m^2\n')

    def Perimetro(self):
        a = 2*self.largura + 2*self.altura
        print(a,'m\n')

    def Medidas (self,altura,largura):
        self.largura = largura
        self.altura = altura


    def AreaPiso(self):
        self.area = self.largura * self.altura
        return self.area

class Sala:

    def __init__(self,comprimento,profundidade):
        self.comprimento = comprimento
        self.profundidade = profundidade



    def TamanhoSala(self,comprimento,profundidade):
        self.comprimento = comprimento
        self.profundidade = profundidade


    def AreaSala(self):
        self.area = self.comprimento * self.profundidade
        return self.area


while True:

    try:
        x = input('Medida do piso no formato mxm: ')
        x = x.replace(',', '.')
        x = x.split('x')
        p = Piso(float(x[0]),float(x[1]))
        a_p = p.AreaPiso()
        print()

        y = input('Medida da sala no formato mxm: ')
        y = y.replace(',', '.')
        y = y.split('x')
        s = Sala(float(y[0]), float(y[1]))
        a_s = s.AreaSala()
        print()

        total = math.ceil(a_s/a_p)

        print(f'Serão nessessárias {total} peças\n\n')

    except:
        print('Comando Inválido\n')

