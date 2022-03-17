#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

b = int(input('Quantos números você deseja imprimir? '))

c = input('Deseja imprimira na vertical (v) ou horizontal (h)? ')


def vertical(b):
    a = 0
    for i in range(b):
        a = a + 1
        print(a)


def horizontal(b):
    a = 0
    l =[]
    for i in range (b):
        a = a + 1
        print(a, end=' ')

if c == 'v':
    vertical(b)
elif c == 'h':
    horizontal(b)

