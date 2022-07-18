# Faça um programa que carregue uma lista com os modelos de cinco carros
# (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros,
# isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de
# 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma
# tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios
# e podem mudar a cada execução do programa.
# Comparativo de Consumo de Combustível
#
# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5
#
# Relatório Final
#  1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
#  2 - gol             -   10.0 -  100.0 litros - R$ 225.00
#  3 - uno             -   12.5 -   80.0 litros - R$ 180.00
#  4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
#  5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.

lst_veiculo = []
lst_km = []

while True:
    veiculo = input('Veículo: ')
    if veiculo == '0':
        break
    else:
        lst_veiculo.append(veiculo)
    try:
        km = float(input('Kilometros por litro: '))
        lst_km.append(km)
    except:
        print('Valor Inválido')


index_eco = lst_km.index(max(lst_km))

with open('Relatório_veículos','w') as rlt:
    rlt.write('Relatório filnal\n')

with open('Relatório_veículos','a') as rlt:
    for i in range(len(lst_km)):
        rlt.write(f'{i+1} - {lst_veiculo[i]:<10}  {lst_km[i]}   litros por Km\n')


with open('Relatório_veículos','a') as rlt:
    rlt.write(f'\n\nO mais econoômico é o {lst_veiculo[lst_km.index(max(lst_km))]} com {lst_km[index_eco]} Km por litro\n')