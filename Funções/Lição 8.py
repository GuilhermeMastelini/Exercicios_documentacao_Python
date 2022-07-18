#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def Digitos(n):
    s = 0

    n = str(n)
    for i in n:
        s += 1

    return(s)

while True:
    try:
        a = int(input('Digite um inteiro: '))
        b = Digitos(a)
        print(f'\nO valor possui {b} digitos')
        break

    except:
        print('A entrada não corresponde a um inteiro.\n')

