# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
import Limpeza as lp

l_mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

l_temp = []

for i in range (12):
    a = input(f'Temperatura média do mês de {l_mes[i]}: ')
    a = lp.limp(a)
    l_temp.append(a)

media = sum(l_temp)/12
print(type(media))
media = '{:.1f}'.format(media)
print(type(media))
media = float(media)
print(type(media))
media_int = int(media)

print(f'A temperaduta média anual foi de {media}°')

l_acima = []
print()

for i in range(12):

    if l_temp[i] > media_int:
        print(f'A temperatura do mês de {l_mes[i]} foi acima da média')
        print()


