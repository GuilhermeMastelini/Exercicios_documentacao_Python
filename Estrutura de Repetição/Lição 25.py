# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera
# verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
s = 0
l = []
while True:
    try:
        n = int(input('Digite o número de pessoas: '))
        break
    except:
        print('Comando Inválido\nTente novamente')

for i in range(n):
    try:
        a = int(input(f'Digite a idade da {i+1}º pessoa: '))
    except:
        print('Idade não identificada. Digite um número inteiro positivo')
    l.append(a)

for x in range(len(l)):
    s += l[x]

resultado = s/n

if resultado <= 25:
    print('A turma é jovem')

elif (resultado > 25) and (resultado <= 60):
    print('A turma é adulta')
else:
    print('A turma é idosa')
