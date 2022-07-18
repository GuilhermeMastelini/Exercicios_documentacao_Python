#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação
# de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes
# valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou.
# O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor
# de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa
# deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
# O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
# Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

l_pagamento = []

def valorPagamento(p,d):

    if d == 0:
        x = p
        return(x)

    else:
        x = p + p * 0.03 + (p * 0.01) * d
        return(x)


while True:

    try:
        p = input('Valor da prestação: ')
        if p == '0':
            break
        p = p.replace(',','.')
        p = float(p)
        d = int(input('Dias de atraso: '))

        valor = valorPagamento(p,d)
        l_pagamento.append(valor)
        valor = '{:.2f}'.format(valor)
        valor = valor.replace('.',',')
        print(f'Valor a ser pago R$ {valor}')
        print()

    except:
        print('comando inválido')

print()
soma = sum(l_pagamento)
soma = '{:.2f}'.format(soma)
soma = soma.replace('.',',')

print(f'Valor total a ser pago R$ {soma}')

