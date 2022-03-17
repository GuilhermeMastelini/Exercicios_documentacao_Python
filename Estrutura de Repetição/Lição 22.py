# Altere o programa de cálculo dos números primos, informando,
# caso o número não seja primo, por quais número ele é divisível.


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

print(l1)
