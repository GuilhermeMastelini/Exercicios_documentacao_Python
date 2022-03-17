#Faça um Programa que leia três números e mostre o maior e o menor deles
print('Insira três números diferentes')
print('Letras e carcateres especiais não são válidos')
a = input('Digite aqui o primeiro número: ')
b = input('Digite aqui o segundo número: ')
c = input('Digite aqui o terceiro número: ')

# limpeza dos números

a = a.strip()
a = a.replace(',','.')
b = b.strip()
b = b.replace(',','.')
c = c.strip()
c = c.replace(',','.')

# verificação se as variáveis receberam apenas números
ver_igual1 = (a == b)
ver_igual2 = (a == c)
ver_igual3 = (b == c)
ver_123 = (not (ver_igual1)) and (not(ver_igual2)) and (not(ver_igual3))
z = 0


if ver_123 == True:
    z = 1

if z == 1:

    a_menor = (a<b) and (a<c)
    b_menor = (b<c) and (b<a)
    c_menor = (c<a) and (c<b)

    if a_menor == True:
        a = str(a)
        a = a.replace('.',',')
        print('{} é menor número'.format(a))

    elif b_menor == True:
        b = str(b)
        b = b.replace('.', ',')
        print('{} é menor número'.format(b))

    elif c_menor == True:
        c = str(c)
        c = c.replace('.', ',')
        print('{} é menor número'.format(c))
    z = 2

if z == 2 :

    a_maior = (a > b) and (a > c)
    b_maior = (b > c) and (b > a)
    c_maior = (c > a) and (c > b)

    if a_maior == True:
        a = str(a)
        a = a.replace('.', ',')
        print('{} é maior número'.format(a))

    elif b_maior == True:
        b = str(b)
        b = b.replace('.', ',')
        print('{} é maior número'.format(b))

    elif c_maior == True:
        c = str(c)
        c = c.replace('.', ',')
        print('{} é maior número'.format(c))

    else:
        print('Erro')

else:
    print('ERRO')
