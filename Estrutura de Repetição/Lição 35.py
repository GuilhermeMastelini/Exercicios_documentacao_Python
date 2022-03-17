#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos
# números primos existentes entre 1 e um número inteiro informado pelo usuário.

lp = []
ver = False

# Verificador de primos
def primo(x,v):
    cont = 0
    for ii in range(x):
        rd = x % (ii + 1)
        if rd == 0:
            cont += 1
    if cont == 2:
        v = True

    return v


#Entrada do valor
while True:
    try:
        a = int(input('Insira um número natural: '))
        if a > 0:
            break
    except:
        print('ERR0')

# Criação da lista de valores
b = 0
for i in range(a):
    ver = False
    b += 1
    ver = primo(b,ver)

    if ver == True:
        lp.append(b)




print(f'Lista de primos {lp}')
