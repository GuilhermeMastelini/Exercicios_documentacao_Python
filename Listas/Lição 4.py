#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

l = ['s','c','x','d','r','e','c','q','a','i']

s = 0

for i in l:

    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        s += 1


print(f'{s} vogais')

