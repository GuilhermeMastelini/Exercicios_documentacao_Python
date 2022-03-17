# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro
# fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou
# para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de
# testes (divisões) executados.
import math
s = 0
p = 0
sds = 0
div = 0

l = []

a = int(input('Num: '))

for x in range(a):
    l.append(x+1)

l.pop(0)
q = len(l)

#print(l)
lp = []

for z in range(q):
    b = l[z]
    for i in range (b):
        divisao = b/(i+2)
        div += 1
        div_truc = math.floor(divisao)
        div += 1
        resto = divisao - div_truc
        if resto == 0:
            s += 1

    if (s > 1) or (b < 2) :
        p = 'não primo'
        s = 0
    else:
        p = 'primo'

    if (p == 'primo'):
        lp.append(b)
        s = 0
    else:
        sds =0
print(lp)
print(f'{div} divisões efetuadas')


