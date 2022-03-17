#Faça um programa que peça dois números, base e expoente,
# calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

import Limpeza
r = 1

while True:
    try:
        b = input('Digite a base: ')
        b = Limpeza.limp(b)
        break
    except:
        print('Valor inválido')


while True:
    try:
        e = input('Digite o expoente: ')
        e = int(e)
        break
    except:
        print('Valor inválido')

for i in range(e):
    r = r * b
print(r)