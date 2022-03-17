#Faça um Programa para um caixa eletrônico.
# O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais,
# o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais,
# o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1

import math

print('Notas disponíveis 100, 50, 10, 5 e 1')
valor = int(input('Digite o valor que deseja sacar: R$ '))

notas_cem = math.floor(valor/100)
restcem = valor%100

notas_ciquenta = math.floor(restcem/50)
restcinquenta = restcem%50

notas_dez = math.floor(restcinquenta/10)
restdez = restcinquenta%10

notas_cinco = math.floor(restdez/5)
restcinco = restdez%5

notas_um = restcinco

print(' ')
if notas_cem >= 1:
    if notas_cem == 1:
        print('{} nota de 100 reais'.format(notas_cem))
    else:
        print('{} notas de 100 reais'.format(notas_cem))
else:
    print(' ')
if notas_ciquenta >= 1:
    if notas_ciquenta == 1:
        print('{} nota de 50 reais'.format(notas_ciquenta))
    else:
        print('{} notas de 50 reais'.format(notas_ciquenta))
else:
    print(' ')

if notas_dez >= 1:
    if notas_dez == 1:
        print('{} nota de 10 reais'.format(notas_dez))
    else:
        print('{} notas de 10 reais'.format(notas_dez))
else:
    print(' ')

if notas_cinco >= 1:
    if notas_cinco == 1:
        print('{} nota de 5 reais'.format(notas_cinco))
    else:
        print('{} notas de 100 reais'.format(notas_cinco))
else:
    print(' ')

if notas_um >= 1:
    if notas_um == 1:
        print('{} nota de 1 real'.format(notas_um))
    else:
        print('{} notas de 1 real'.format(notas_um))
else:
    print(' ')
