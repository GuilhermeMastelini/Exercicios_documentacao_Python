#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

s = 0
l = []
print('Para encerrar pressione x')
while True:

    a = input('Digite um número entre 1 e 100: ')
    x = (a == 'x') or (a == 'X')
    if x == True:
        break
    else:
        try:
            a = a.strip()
            a = a.replace(',','.')
            a = float(a)
            if ((a >= 1) and (a <= 100)):
                l.append(a)
                print('Adicionado')
            else:
                print('número inválido')
        except:
             print('número inválido')

l.sort()
print(l)

for i in range(len(l)):
    s1 = l[i]
    s = s1 + s

print(f'O menor valor é {l[0]}, o maior valor é {l[-1]} e a soma é {s}')
