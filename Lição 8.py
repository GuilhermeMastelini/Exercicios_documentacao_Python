#Faça um programa que leia 5 números e informe a soma e a média dos números.

import Limpeza
a = int(input('Quantos números você deseja inserir? '))

s = 0

for i in range(a):
    c = input(f'Digite o {i+1}º valor: ')
    c = Limpeza.limp(c)
    s = s + c

media = s/a
media = '{:.1f}'.format(media)
print(media)
