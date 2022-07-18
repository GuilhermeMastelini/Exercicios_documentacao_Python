# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

import random as rd

l = []

for i in range (10):
    ll = []

    for y in range (4):
        a = rd.randrange(0,11,1)
        ll.append(a)
    l.append(ll)

medias = []

s = 0

for i in range(10):
    b = sum(l[i])/4
    medias.append(b)

    if b >= 7:
        s += 1


print(medias)
print(f'{s} alunos tiveram média azul')