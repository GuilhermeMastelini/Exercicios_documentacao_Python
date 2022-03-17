# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
# o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
# regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
# multa de R$ 4,00 por quilo excedente. João precisa que você
# faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável
# multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

a = input('Digite o valor em Kg ')
a = a.replace(',', '.')
a = a.strip()
a = float(a)

if a <= 50:
    print('Sua pesca de {:.3} Kg está isenta de impostos.'. format(a))

elif a > 50:
    b = a - 50
    c = 4*b
    print('Sua pesca excedeu  o limite em {} Kg. Você pagará R$ {:.2f} por esse valor'.format(b,c))
