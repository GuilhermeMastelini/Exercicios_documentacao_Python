#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato

x = input('Informe o valor do 1º produto: ')
y = input('Informe o valor do 2º produto: ')
z = input('Informe o valor do 3º produto: ')
x = x.strip()
x = x.replace(',','.')
x = float(x)
y = y.strip()
y = y.replace(',','.')
y = float(y)
z = z.strip()
z = z.replace(',','.')
z = float(z)
x = '{:.2f}'.format(x)
y = '{:.2f}'.format(y)
z = '{:.2f}'.format(z)

xv = (x<y) and (x<z)
yv = (y<x) and (y<z)
zv = (z<x) and (z<y)

if xv == True:
    x = str(x)
    x = x.replace('.',',')
    print('O 1º produto é o mais barato, no valor de R$ {}'.format(x))

elif yv == True:
    y = str(y)
    y = y.replace('.', ',')
    print('O 1º produto é o mais barato, no valor de R$ {}'.format(y))

elif zv == True:
    z = str(z)
    z = z.replace('.', ',')
    print('O 1º produto é o mais barato, no valor de R$ {}'.format(z))

else:
    print('Erro')