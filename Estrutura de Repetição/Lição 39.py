# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o
# segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
# Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

lista_altura = []


for i in range(10):
    try:
        print(f'Aluno {i+1}')
        altura = input('Digite a altura em metros: ')
        altura = altura.replace(',','.')
        altura = float(altura)
        lista_altura.append(altura)

    except:
        print('comando inválido')
maior = max(lista_altura, key=float)
menor = min(lista_altura, key = float)

print(f'O maior é aluno é o {lista_altura.index(maior)+1}')
print(f'O menor é aluno é o {lista_altura.index(menor)+1}')

