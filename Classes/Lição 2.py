#Classe Quadrado: Crie uma classe que modele um quadrado:
#
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:

    def __init__(self,lado):
        self.lado = lado

    def MudarLado(self,lado):
        self.lado = lado
        print(f'Valor do lado alterado para {self.lado}\n')

    def RetornaLado(self):
        print(self.lado)
        print()

    def Area(self):
        print(self.lado**2)
        print()

quadrado_1 = Quadrado(4)

while True:

    a = int(input('(1)Muda Lado\n(2)Retorna Lado\n(3)Calcula Área\n\n'))

    if a == 1:
        b = float(input('Novo valor: '))
        quadrado_1.MudarLado(b)

    elif a == 2:
        quadrado_1.RetornaLado()

    elif a == 3:
        quadrado_1.Area()

    else:
        print('Comando Inválido\n')

