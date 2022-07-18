# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.


def Reverso(n):

    l = []
    ll = []
    n = str(n)

    for i in n:
        l.append(i)

    for i in range(len(l)):
        ll.append(l[(i+1)*-1])


    return(ll)


while True:

    try:
        a = int(input('Informe um inteiro: '))

        x = Reverso(a)
        print(*x, sep='')


    except:
        print('\nComando Inválido\n')
