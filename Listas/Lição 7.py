# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

import random as rd
v = []
for i in range(5):
    w = rd.randrange(0,100,1)
    v.append(w)


soma = sum(v)

produto = 1

for i in v:
    produto *= i

print(f'Soma {soma}\nProduto {produto}\n')
print(*v, sep=', ')