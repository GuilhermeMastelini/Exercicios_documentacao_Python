import os ,  sys
# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela media dos cinco valores restantes.
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
# depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado
# o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo
#
# Primeiro Salto: 6.5m
# Segundo Salto: 6.1m
# Terceiro Salto: 6.2m
# Quarto Salto: 5.4m
# Quinto Salto: 5.3m
#
# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dossaltos: 5.9m

l_geral = []

while True:

    a = input('Nome do atleta: ')

    if a == '':
        break

    else:

        try:
            l = []
            for i in range (5):
                s = input(f'Salto número {i+1}: ')
                s = s.replace(',','.')
                s = float(s)
                l.append(s)


            print(f'\nAtleta: {a}\nSaltos: {l[0]} - {l[1]} - {l[2]} - {l[3]} - {l[4]}\nMédia = {sum(l)/5}m\n\n')

            l_geral.append([a,sum(l)/5,l])

        except:
            print('Comando Inválido')

print(l_geral)

with open ('Relatório_saltos.txt','w') as rlt:
    for i in range(len(l_geral)):
        nome = l_geral[i][0]
        media = l_geral[i][1]
        saltos = l_geral[i][2]
        rlt.write(f'{nome},   média   {media}         saltos {saltos}\n')
