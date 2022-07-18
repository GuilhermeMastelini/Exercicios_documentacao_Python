# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

l_idade = []
l_altura = []
print('Idade = 0, encerra o programa')


while True:

    try:
        a = int(input('Digite a idade: '))

        if a == 0:
            break

        else:
            l_idade.append(a)
            b = input('Digite a altura: ')
            b = b.strip()
            b = b.replace(',','.')
            b = float(b)
            l_altura.append(b)
            print()

    except:
        print('Comando Inválido')

media = sum(l_altura)/len(l_altura)
print(f'Média das alutras {media}m')
s = 0

for i in range(len(l_idade)):
    if l_idade[i] > 13:
        if l_altura[i] < media:
            s += 1


print(f'{s} alunos acima dos 13 anos estão abaixo da média das alturas')