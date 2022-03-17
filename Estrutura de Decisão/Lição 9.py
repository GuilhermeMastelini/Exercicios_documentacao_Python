#Faça um Programa que leia três números e mostre-os em ordem decrescente.
a = int(input('Digite quantos números você deseja ordenar: '))
x = []

for i in range(1, a +1):
    v = int(input('Digite o {}º número: '.format(i)))
    x.append(v)
    i = i+1
x.sort(reverse = True)
print(x)
x.sort()
print(x)
