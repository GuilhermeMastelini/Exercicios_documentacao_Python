# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
# PAR e os números IMPARES no vetor impar. Imprima os três vetores.
import random as rd

v = []

v_par = []

v_impar = []

for i in range(20):
    n = rd.randrange(1,100)
    v.append(n)

    if n % 2 == 0:
        v_par.append(n)

    else:
        v_impar.append(n)


print()
print(v)
print()
print(v_par)
print(v_impar)