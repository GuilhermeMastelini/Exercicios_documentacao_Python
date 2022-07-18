# Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000,
# ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores
# receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

import random as rd

l = []

print('Escolha a faixa salarial:\n '
      '\n (1) $200 - $299'
      '\n (2) $300 - $399'
      '\n (3) $400 - $499'
      '\n (4) $500 - $599'
      '\n (5) $600 - $699'
      '\n (6) $700 - $799'
      '\n (7) $800 - $899'
      '\n (8) $900 - $999 '
      '\n (9) $1000 em diante')

for i in range (500):
    x = rd.randrange(200,2000)
    l.append(x)

l.sort()

while True:
    try:
        q = int(input('Faixa: '))

        if 1 <= q <= 9:
            break
        else:
            print('Número Inválido')

    except:
        print('Comando Inválido')



valor = 100 + q * 100

print(l)

for i in range(len(l)):

    if  valor <= l[i] < valor + 100:
        print(i + 1)

