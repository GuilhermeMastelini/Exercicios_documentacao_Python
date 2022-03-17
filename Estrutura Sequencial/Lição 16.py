#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
import math

print('Bem vindo a nossa loja de tintas ')
a = int(input('Selecione como você quer informar a metragem à ser pintada: \n (1) para área em metros quadrados \n (2) para largura x altura em metros \n '))
b = int (input('Informe o número de paredes: '))
# s é o somatório das áreas das paredes
s = 0
# x é o valor do total da tinta acrescido de 10%
x = 0

#salario_bruto = '{:.2f}'.format(salario_bruto)
if a == 1:
    for i in range(1,b+1):
        c = input('Digite a área da {}º parede: '.format(i))
        c = c.strip()
        c = c.replace(',','.')
        c = float(c)
        s += c

elif a ==2:
    for i in range (1,b+1):
        c = input('Digite a largura da {}º parede: '.format(i))
        d = input('Digite a altura da {}º parde: '.format(i))
        c = c.strip()
        d = d.strip()
        c = c.replace(',','.')
        d = d.replace(',','.')
        c = float(c)
        d = float(d)
        e = c * d
        s += e
else:
    print('Comando Invalido')

# 1 litro pinta 6m2
tinta_litros = s/6

lt18 = tinta_litros/18
lt18 = math.ceil(lt18)

lt36 = tinta_litros/(3.6)
lt36 = math.ceil(lt36)

#valores da combinação das latas
x = tinta_litros
x = x*1.1
l1 = x/18
l1 = math.floor(l1)
l2 = x%18
l2 = l2 / 3.6
l2 = math.ceil(l2)
total = (l1*80)+(l2*25)

print('Você pode comprar {} latas de 18 litros no valor de R$ 80,00 cada \n Somando o total de R$ {}'.format(lt18,lt18*80))
print('Você pode comprar {} latas de 3,6 litros no valor de R$ 25,00 cada \n Somando o total de R$ {}'.format(lt36,lt36*25))
print('Você pode comprar {} latas de 18 litros no valor de R$ 80,00 cada \n '
      'e {} latas de 3,6 litros no valor de R$ 25,00 \n Somando o total de R$ {}'.format(l1, l2, total))