# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma
# dos quadrados dos elementos do vetor.

import random as rd
l = []
l_q = []

for i in range (10):
    a = rd.randrange(1,20,1)
    b = a**2
    l.append(a)
    l_q.append(b)

print(l)
print()
print(l_q)
print()

print(sum(l_q))