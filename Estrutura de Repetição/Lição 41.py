# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
# valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25

import Limpeza as lp

divida = input('Valor da dívida R$ ')
divida = lp.limp(divida)


print('Sua dívida pode ser negociada em :')
print()
print(f'1 vez com 0% de juros totalizando {lp.f_s2(divida)}')
juros = 10
for i in range(3,13,3):

    parcela = (divida*(1+(juros/100)))/i
    total = divida*(1+(juros/100))
    print(f'{i} vezes com {juros}% em parcelas de R$ {lp.f_s2(parcela)} totalizando R$ {lp.f_s2(total)}')
    juros += 5
