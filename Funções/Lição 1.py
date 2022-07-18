# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
#

while True:
    try:
        a = int(input('Número de valores: '))
        break
    except:
        print('Comando Inválido')

for i in range(a):
    print(f'{i+1} '*(i+1))