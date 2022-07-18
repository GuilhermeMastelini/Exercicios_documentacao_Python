# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lst = []


while True:

    try:
        i = len(lst) + 1
        a = float(input(f'Digite o {i}º número: '))
        lst.append(a)

        if len(lst) == 10:
            break

    except:
        print('Comando Inválido')



print()

for i in range(10):
    x = (i+1) * (-1)
    print(lst[x])