# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

x  = float(input('Dígite um número real: '))

if x > 0 :
    print('{} é um número positivo.'.format(x))
elif x < 0 :
    print('{} é um número negativo.'.format(x))
else :
    print('{} é definido como neutro.'.format(x))
