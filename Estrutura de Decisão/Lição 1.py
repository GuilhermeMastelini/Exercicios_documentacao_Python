#Faça um Programa que peça dois números e imprima o maior deles.

a = input('Digite um número: ')
b = input('Digite mais um número: ')
a = a.strip()
a = a.replace(',','.')
a = float(a)
b = b.strip()
b = b.replace(',','.')
b = float(b)

if a > b:
    a = str(a)
    a = a.replace('.',',')
    b = str(b)
    b = b.replace('.', ',')
    print('O número {} é maior que o número {}'.format(a,b))

else:
    a = str(a)
    a = a.replace('.', ',')
    b = str(b)
    b = b.replace('.', ',')
    print('O número {} é maior que o número {}'.format(b,a))

