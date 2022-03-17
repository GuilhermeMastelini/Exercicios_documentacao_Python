#Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).

a = int(input('Digite um número: '))
b = a%2

if b == 0:
    print('{} é um número par.'.format(a))
else:
    print('{} é um número impar.'.format(a))
