#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
# Dica: utilize uma função de arredondamento.
import Limpeza
import math

a = input('Digite um número: ')
a = Limpeza.limp(a)

b = math.floor(a)

c = a-b

if c == 0:
    a = int(a)
    print('O número {} é inteiro'.format(a))
else:
    a = Limpeza.f_p(a)
    print('O número {} é racional'.format(a))
