#Faça um programa que leia 5 números e informe o maior número.

def limp(x):
    x = x.strip()
    x = x.replace(',','.')
    x = float(x)
    return x

a = int(input('Quantos números você deseja inserir? '))
l = []

for i in range(a):
    b = input(f'Digite o {i+1}º número: ')
    b = limp(b)
    l.append(b)
l.sort(reverse = True)
print(l[0])
