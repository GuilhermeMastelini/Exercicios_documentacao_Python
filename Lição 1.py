#Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que
# o usuário informe um valor válido.
import Limpeza

verificacao = False

while (verificacao ==  False):
    a = input('Digite uma nota de 0 à 10: ')
    try:
        a = Limpeza.limp(a)
    except:
        a = -2

    b = (a >= 0) and (a <= 10)

    if b == True:
        a = Limpeza.f_s1(a)
        print('Nota {} computada'.format(a))
        verificacao = True

    else:
        print('Valor invalido')
