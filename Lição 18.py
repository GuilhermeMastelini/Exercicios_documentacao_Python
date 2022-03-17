#Faça um programa que, dado um conjunto de N números, determine o menor valor,
# o maior valor e a soma dos valores.

s = 0
l = []
print('Para encerrar pressione x')
while True:

    a = input('Digite um número: ')
    x = (a == 'x') or (a == 'X')
    if x == True:
        break
    else:
        try:
            a = a.strip()
            a = a.replace(',','.')
            a = float(a)
            l.append(a)
            print('Adicionado')
        except:
             print('número inválido')

l.sort()
print(l)

for i in range(len(l)):
    s1 = l[i]
    s = s1 + s

print(f'O menor valor é {l[0]}, o maior valor é {l[-1]} e a soma é {s}')
