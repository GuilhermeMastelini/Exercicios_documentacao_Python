# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
# Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

lista_cidade = []
lista_veiculos = []
#lista de acidentes geral
lista_acidentes1 = []
#lista de acidentes em cidades com menos de 2.000 veiculos
lista_acidentes2 = []


# entrada de dados
for i in range(5):

    cidade = input(f'Nome da {i+1}º cidade: ')
    lista_cidade.append(cidade)

    veiculos = int(input('Número de veículos: '))
    lista_veiculos.append(veiculos)

    acidentes = int(input('Número de acidentes: '))
    lista_acidentes1.append(acidentes)

    if veiculos < 2000:
        lista_acidentes2.append(acidentes)

# variáveis de menor e maior indice de acidentes
menor_i_a = min(lista_acidentes1, key = int)
maior_i_a = max(lista_acidentes1, key = int)
index_menor = lista_acidentes1.index(menor_i_a)
index_maior = lista_acidentes1.index(maior_i_a)

media_veiculos = sum(lista_veiculos)/5

media_acidentes = sum(lista_acidentes2)/len(lista_acidentes2)
media_acidentes = '{:.2f}'.format(media_acidentes)

print(f'O maior índice de acidentes foi na cidade {lista_cidade[index_maior]}, com {maior_i_a} acidentes')
print(f'O menor índice de acidentes foi na cidade {lista_cidade[index_menor]}, com {menor_i_a} acidentes')
print(f'A média de veículos é de {media_veiculos}')
print(f'A média de acidentes nas cidades com menos de 2000 veículos é de {media_acidentes} acidentes')
