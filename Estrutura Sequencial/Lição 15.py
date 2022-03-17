#Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

s = 0
a = int(input('Deseja informar a área (1) ou a metragem da parede (2)? '))
print('INFORME TODOS OS VALORES EM METROS OU METROS QUADRADOS')

if a == 1:
    b = int(input('Quantas paredes deseja pintar? '))
    for i in range(1,b+1):
        c = str((input('Qual é a área da {} parede? '.format (i))))
        c = c.replace(',','.')
        c = c.strip()
        c = float(c)
        s = s + c
        t = s * (1 / 3)
        l = t / 18
        l = math.ceil(l)
        print('{} latas de 18l é o recomendado '.format(l))

elif a == 2:
    b = int(input('Quantas paredes deseja pintar? '))
    for i in range( 1, b+1 ):
        c = str(input('Qual é a altura da {} parede? '.format (i)))
        d = str(input('Qual é a largura da {} parede? '.format(i)))
        c = c.replace(',','.')
        c = c.strip()
        c = float(c)
        d = d.replace(',', '.')
        d = d.strip()
        d = float(d)
        s = s + (c*d)
        t = s * (1 / 3)
        l = t / 18
        l = math.ceil(l)
        print('{} latas de 18l é o recomendado '.format(l))
else:
    print('Comando Inválido')
