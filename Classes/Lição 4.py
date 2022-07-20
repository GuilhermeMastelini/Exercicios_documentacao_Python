#Classe Pessoa: Crie uma classe que modele uma pessoa:
#
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:

    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        print(f'\n{self.nome}, {self.idade} anos, {self.peso}Kg, {self.altura} metros\n\n')

    def Envelhecer(self):

        self.idade += 1

        if self.idade < 22:
            self.altura += 0.05

        print(f'\n{self.nome}, {self.idade} anos, {self.peso}Kg, {self.altura} metros\n\n')

    def Engordar(self,kilos):

        self.peso = self.peso + kilos
        print(f'\n{self.nome}, {self.idade} anos, {self.peso}Kg, {self.altura} metros\n\n')

    def Emagrecer(self,kilos):
        self.peso = self.peso - kilos
        print(f'\n{self.nome}, {self.idade} anos, {self.peso}Kg, {self.altura} metros\n\n')

    def Crescer(self,metros):

        self.altura = self.altura + metros
        self.peso = self.peso + 1
        print(f'\n{self.nome}, {self.idade} anos, {self.peso}Kg, {self.altura} metros\n\n')

print('Criar Pessoa:\n')
nome = input('Nome: ')
idade = int(input('Idade: '))
peso = float(input('Peso: '))
altura = float(input('Altura: '))
p1 = Pessoa(nome,idade,peso,altura)

while True:

    print('(1)Envelhecer\n(2)Engordar\n(3)Emagrecer\n(4)Crescer\n\n')
    x = input('Escolha a função desejada: ')

    if x == '1':
        p1.Envelhecer()

    elif x == '2':
        k = float(input('Quantos kilos? '))
        p1.Engordar(k)

    elif x == '3':
        k = float(input('Quantos kilos? '))
        p1.Emagrecer(k)

    elif x == '4':
        m = float(input('Quantos metros? '))
        p1.Crescer(m)
