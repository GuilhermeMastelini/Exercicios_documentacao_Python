#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com
# o nome do mês por extenso.

# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.


l_mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

a = input('Data: ')
s = a.split('/')

print(s)

dia = s[0]

index = int(s[1])-1

mes = l_mes[index]

print(f'Você nasceu em {dia} de {mes} de {s[2]}')
