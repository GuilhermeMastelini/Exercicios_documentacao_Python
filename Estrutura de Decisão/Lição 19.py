#Faça um Programa que leia um número inteiro menor que 1000 e imprima a
# quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

a = input('Digite um número inteiro: ')
b = len(a)


uni = (b == 1)
dez = (b == 2)
cent = (b == 3)



if uni == True:

    if a == '1':
        print('{} unidade'.format(a))
    else:
        print('{} unidades'.format(a))


elif dez == True:
    s1 = (a[0] == '1')

    s3 = (a[1] == '1')


    if s1 == True:
        c = ' '
    else:
        c = 's'

    if s3 ==True:
        d = ' '
    else:
        d = 's'

    print('{} dezena{} e {} unidade{}'.format(a[0],c,a[1],d))



elif cent == True:
    if a[0] == '1':
        c = ' '
    else:
        c = 's'

    if a[1] == '1':
        d = ' '
    else:
        d = 's'
    if a[2] == '1':
        e = ' '
    else:
        e = 's'

    print('{} centena{}, {} dezena{} e {} unidade{}'.format(a[0],c,a[1],d,a[2],e))
