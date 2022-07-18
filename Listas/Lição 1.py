#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

lista = []
for i in range(5):
    a = int(input(f'Isira o {i+1}º número: '))
    lista.append(a)

for ii in range(len(lista)):
    print(lista[ii])

