#Faça um Programa que peça um número correspondente a um determinado ano
# e em seguida informe se este ano é ou não bissexto.

a = int(input('Digite o ano: '))

v1 = a%4
v2 = a%100

bv1 = (v1 == 0)
bv2 = (v2 == 0)
ver = bv1 or bv2


if ver == True:
    print('{} é um ano bissexto'.format(a))
else:
    print('{} não é um ano bissexto'.format(a))
