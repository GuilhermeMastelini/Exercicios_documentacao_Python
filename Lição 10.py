#Faça um programa que receba dois números inteiros e gere os números inteiros
# que estão no intervalo compreendido por eles.

while True:
    try:
        a = int(input('Digite o primeiro número: '))
        break
    except:
        print('Comando inválido')

while True:
    try:
        b = int(input('Digite o segundo número: '))
        break
    except:
        print('Comando inválido')

for i in range(a,b+1,1):
    print(i)
