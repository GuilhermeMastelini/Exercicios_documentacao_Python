#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
# números pares e a quantidade de números impares.

lp = []
li = []
ver = 0

while ver < 10:
    try:
        a = int(input('Digite um inteiro: '))
        if a%2 == 0:
            lp.append(a)

        else:
            li.append(a)
    except:
        print('Comando inválido')

    ver = len(lp) + len(li)

print(f' {len(lp)} pares \n {len(li)} impares')
