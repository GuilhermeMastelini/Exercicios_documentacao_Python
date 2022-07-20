# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
#
# Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma
# combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para
# armazenar esta informação por que ela pode ser calculada a qualquer momento.

import random as rd

class Tamagushi:

    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 10
        self.idade = 0
        self.humor = 10
        self.meses = 0
        self.sorte = 0

    # Função de alimentar
    def Comida(self):

        if self.fome == 0:
            print(f'Tamagushi {self.nome} está cheio!!! \nEle Vomitou!!')
            self.saude -= 1
        else:
            self.fome -= 2
            print(f'Tamagushi {self.nome} está comendo!\n')



    # Função de cura
    def Remedio(self):

        if self.saude == 10:
            print(f'Não se deve usar remédios sem precisar!!!\nTamagushi {self.nome} passou mal!!!')
            self.saude -= 3
        else:
            print(f'Tamagushi {self.nome} está se recuperando... Continue o tratamento')
            self.saude += 1



    # Confere o humor
    def Humor(self):


        if self.humor < 10:
            self.humor += 1
            print(f'Tamagushi {self.nome} está feliz!!')

        if self.fome > 5:
            self.humor -= 1
            print(f'Tamagushi {self.nome} está com Fome! Isso o deixa de mal humor')


        if self.humor < 3:
            print(f'Tamagushi {self.nome} está estressado!!! Isso prejudica sua saúde!')
            self.saude -= 1



    # Brincar, melhora humor
    def Bricar(self):

        if self.saude < 5:
            print(f'Tamagushi {self.nome} não está bem de saúde! Você estressou ele!!')
            self.humor -= 1
        else:

            if self.fome > 6:
                print(f'Tamagushi {self.nome} está com fome! Ele não quer brincar!')
                self.humor -= 1

            else:
                print(f'Tamagushi {self.nome} está ficando feliz! Ele te ama')
                self.humor += 1


    # Código que corre a cada rodada

    def Vida (self):

        if self.meses == 5:
            self.idade += 1
            self.meses = 0

        if self.idade == 5:
            print(f'Tamagushi {self.nome} morreu de causas naturais')
            quit()

        if self.humor == 0:
            print(f'Tamagushi {self.nome} morreu de colápso nervoso')
            quit()

        if self.fome == 10:
            print(f'Tamagushi {self.nome} morreu de fome')
            quit()

        if self.saude == 0:
            print(f'Tamagushi {self.nome} morreu de uma doença que poderia ser tratada')


        self.meses += 1
        self.fome +=1
        print(f'Saúde {self.saude}      Fome  {self.fome}       Humor  {self.humor}      Idade     {self.idade}\n\n')

    def Sorte(self):
        self.sorte = rd.randrange(1,100,1)

        if self.sorte == 50:
            print(f'Tamagushi {self.nome} morreu de causas naturais')
            quit()

        if self.sorte > 90:
            self.saude -= 3

        if (self.sorte%2) == 1:
            self.humor -=1

a = input('Escolha um nome para seu Tamagushi: ')
tamagushi = Tamagushi(a)

while True:

    try:
        print()
        tamagushi.Sorte()
        tamagushi.Vida()
        print('(1)Para Brincar\n(2)Para Alimentar\n(3)Para dar remédio\n(0)Passar a rodada\n')
        a = input(':')

        if a == '1':
            tamagushi.Humor()

        elif a == '2':
            tamagushi.Comida()

        elif a == '3':
            tamagushi.Remedio()



    except:

        break
