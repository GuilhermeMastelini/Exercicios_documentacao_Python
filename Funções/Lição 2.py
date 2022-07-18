# faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

while True:

    try:
        a = int(input('Valor: '))
        break

    except:
        print('Comando Inválido')


for i in range(a):
    l = []

    for x in range(i+1):
        l.append(x+1)
    print(*l, sep = ' ')
