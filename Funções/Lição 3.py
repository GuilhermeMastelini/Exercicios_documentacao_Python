# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

a = int(input('Valor: '))
b = int(input('Valor: '))
c = int(input('Valor: '))


def Soma (x,y,z):

    s = x + y + z
    return (s)

w = Soma(a,b,c)

print(w)