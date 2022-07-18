#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os
# carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer
# outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em
# caixa alta ou caixa baixa, independentemente de como foram digitados.

import random as rd


while True:

    a = input('Palavra: ')
    a = 'abcdefgh'
    l_1 = []
    l_2 = []

    for i in a:
      l_1.append(i)

    for y in range(len(l_1)):

        r = rd.randrange(0,len(l_1),1)

        l_2.insert(r,l_1[y])

    print()
    print(*l_2)
    print()

