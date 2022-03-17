#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
# de maças adquiridas e escreva o valor a ser pago pelo cliente.

import Limpeza

def limpp(x):
    x = x.strip()
    x = x.upper()
    x = x.replace('Ã','A')
    return x
pm = 0
mq = 0
cq = 0
pc = 0

print('Responda com sim ou não')

m = input('Deseja morango? ')
m = limpp(m)

if m == 'SIM':
     mq = input('Quantos Kilos? ')
     mq = Limpeza.limp(mq)

     if mq < 5:
         pm = mq * 2.5
     else:
         pm = mq * 2.2

else:
    print(' ')

c = input('Deseja maça? ')
c = limpp(c)

if c == 'SIM':
    cq = input('Quantos Kilos? ')
    cq = Limpeza.limp(cq)

    if cq < 5:
        pc = cq * 1.8
    else:
        pc = cq * 1.5

preco = pc + pm
kg = cq +mq

if (preco > 25) or (kg >= 8):
    print('Você ganhou um desconto especial de 10%')
    preco = Limpeza.f_s2(preco)
    print('Total a pagar R${}'.format(preco))

else:
    preco = Limpeza.f_s2(preco)
    print('Total a pagar R${}'.format(preco))

print('Obrigado pela preferência')
