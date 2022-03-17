# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

import math

l1 = []

a = int(input('Num: '))


for i in range (2,a+1,1):
    b = a/i

    c = math.floor(b)

    d = b - c

    if d == 0:
        l1.append(b)


if (len(l1) > 1) or (a == 0):
    print(f'{a} não um número primo')
else:
    print(f'{a} é um número primo')

