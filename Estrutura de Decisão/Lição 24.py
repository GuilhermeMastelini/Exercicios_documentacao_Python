#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual
# operação ele deseja realizar.
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

import Limpeza
import math

print('Escolha a operação que você deseja realizar \n (1) Soma \n (2) Subtração \n (3) Divisão \n (4) Multiplicação')

operacao = int(input('Digite o código da operação: '))

a = input('Digite o perimeiro número: ')
b = input('Digite o segundo número: ')

a = Limpeza.limp(a)
b = Limpeza.limp(b)

ww = 0
r = 0
erro = False

if operacao == 1:
    r = a+b

elif operacao == 2:
    r = a-b

elif operacao == 3:
    if b == 0:
        print('Erro! Não existe divisão por Zero')
        erro = True
    else:
        r = a/b

elif operacao == 4:
    r = a*b

else:
    print('Erro')

if erro == False:
    rr = math.floor(r)
    x = r-rr

    if x == 0:
        w = 'Inteiro'
        ww = True
    else:
        w = 'Racional'

    if True:
        teste_par = r/2
        teste_par == 0

        if teste_par == True:
            par = 'Par'
        else:
            par = 'Impar'

        if r > 0:
            positivo = 'positivo'
        elif r < 0:
            positivo = 'negativo'
        else:
            positivo = 'Neutro'

        if ww == True:
            r = int(r)
        else:
            r = Limpeza.f_p(r)

        if (w == 'Racional') or (r == 0):
            par = ' '

        print('O resultado da operação é {}'.format(r))
        # par, inteiro, positivo
        print('É um número {}, {} e {}'.format(w, par, positivo))

else:
    print('Fim')
