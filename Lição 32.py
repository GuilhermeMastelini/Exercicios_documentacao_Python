#aça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120

while True:
    try:
        a = int(input('Insira o número que deseja calcular o fatorial: '))
        break
    except:
        print('Erro')

l = []
f = 1
x = 0

for i in range(a):
    x = i+1
    f = f * x
    l.append(x)

l.sort(reverse = True)


for q in range(len(l)):
    l[q] = str(l[q])

b = ' x '.join(l)

print(f'{a}! = {b} = {f}')