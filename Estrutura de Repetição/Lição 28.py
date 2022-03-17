#Faça um programa que calcule o valor total investido por um colecionador em sua coleção
# de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs
# e o valor para em cada um.

a = int(input('Insira a quantidade de cds: '))

s = 0

for i in range(a):
    b = input(f'Insira o valor do {i+1}º CD: R$ ')
    b = b.strip()
    b = b.replace(',','.')
    b = float(b)
    s += b

m = s/a
m = '{:.2f}'.format(m)
m = str(m)
m = m.replace('.',',')

x = '{:.2f}'.format(s)
x = str(x)
x = x.replace('.',',')

print(f'O valor total inverstido foi de R$ {x}\nO preço médio pr CD é de R$ {m}')