# Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene
# os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random
lista =[]

for i in range(100):
    a = random.randrange(1,7)
    lista.append(a)


for ii in range(6):

    print(f'O número {ii+1} aparece {lista.count(ii+1)} vezes')

