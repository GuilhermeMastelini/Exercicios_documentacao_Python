#Faça um programa que calcule o mostre a média aritmética de N notas
soma = 0
l = []
while True:
    try:
        a = int(input('Quantas notas deseja calcular? '))
        break
    except:
        print('Erro, tente novamente')



for i in range(a):
    b = input(f'Digite a {i+1}º nota: ')
    b = b.strip()
    b = b.replace(',', '.')
    b = float(b)
    l.append(b)

w = len(l)
print(l)
for x in range(w):
    soma = soma + l[x]

resp = soma/w
resp = '{:.1f}'.format(resp)
resp = str(resp)
resp = resp.replace('.',',')

print(f'A média é {resp}')