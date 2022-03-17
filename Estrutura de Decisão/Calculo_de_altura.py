import math

h = float(input('Altura do teodolito: '))
a1 = float(input('Ângulo 1: '))
a2 = float(input('Ângulo 2: '))

tg1 = math.tan(a1)
tg2 = math.tan(a2)

f = h*(tg1/tg2)

r = f + h
r = '{:.1f}'.format(r)
print(r)