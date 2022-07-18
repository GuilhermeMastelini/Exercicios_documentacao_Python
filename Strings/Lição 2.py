#Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o
# seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas.
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

name = input('Type your name: ')

l = []

for i in name:

    if len(l) == 0:
        letra = i.upper()
        l.append(i)

    else:
        letra = i.upper()
        l.insert(len(l)*-1, letra)

print(*l)