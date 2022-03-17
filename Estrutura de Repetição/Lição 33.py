# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
# que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior
# temperaturas informadas, bem como a média das temperaturas.
import Limpeza as lp

l = []

print('Insira as temperaturas em Celcius. Digite x para encerrar o programa')

while True:
    try:
        a = input('Digite a temperatura: ').upper()
        if a == 'X':
            break
        else:
            a = lp.limp(a)
            l.append(a)
    except:
        print('Erro')

l.sort()

s = 0

for i in range(len(l)):
    s += l[i]

m = s/(len(l))
m = lp.f_s1(m)

print(f'A maior temperatura é {l[-1]}ºC')
print(f'A menor temperatura é {l[0]}ºC')
print(f'A média das temperaturas é de {m}ºC')