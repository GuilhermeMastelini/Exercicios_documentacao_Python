#Faça um Programa que leia três números e mostre o maior deles.

a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))

v1 = (a>b) and (a>c)
v2 = (b>c) and (b>a)
v3 = (c>a) and (c>b)
v4 = (a == b) and (a>c) and (b>c)
v5 = (a == c) and (a>b) and (c>b)
v6 = (b == c) and (b>a) and (c>a)
v7 = (a == b) and (b == c)

print('Os números escolhidos foram {} , {} e {}'.format(a,b,c))

if v1 == True:
    print('O número {} é o maior entre os três.'.format(a))

elif v2 == True:
    print('O número {} é o maior entre os três.'.format(b))

elif v3 == True:
    print('O número {} é o maior entre os três.'.format(c))

elif v4 == True:
    print('O número {} é o maior (estrada duplicada).'.format(a))

elif v5 == True:
    print('O número {} é o maior (estrada duplicada).'.format(a))

elif v6 == True:
    print('O número {} é o maior (estrada duplicada).'.format(b))

elif v7 == True:
    print('O número {} foi inserido três vezes.'.format(a))

else:
    print('ERRO')
