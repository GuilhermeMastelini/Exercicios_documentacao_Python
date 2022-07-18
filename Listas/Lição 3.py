# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

import Limpeza as lp

notas = []

for i in range(4):
    try:
        a = input(f'Digite a {i+1}º nota: ')
        a = lp.limp(a)
        notas.append(a)
    except:
        print('Comando Inválido')

media = sum(notas)/4
media_limpa = lp.f_s1(media)

for i in range(4):
    nota_limpa = lp.f_s1(notas[i])
    print(f'{i+1}º nota: {nota_limpa}')
print()

print(f'Média final {media_limpa}')