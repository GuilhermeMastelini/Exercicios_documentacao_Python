# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
# contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

s = input('Digite seu salario atual: R$ ')
s = s.strip()
s = s.replace(',','.')
s = float(s)

f1 = s <= 280
f2 = (s > 280) and (s <= 700)
f3 = (s > 700) and (s <= 1500)
f4 = s > 1500

if f1 == True:
    d = 0.2 * s
    d = '{:.2f}'.format(d)
    d = str(d)
    d = d.replace('.',',')
    ns = 1.2 * s
    ns = '{:.2f}'.format(ns)
    ns = str(ns)
    ns = ns.replace('.', ',')
    s = '{:.2f}'.format(s)
    s = str(s)
    s = s.replace('.',',')
    print('Seu antigo salário era de R$ {}'.format(s))
    print('Você recebeu um aumento de 20%')
    print('Você receberá R$ {} à mais'.format(d))
    print('Seu novo salário é de R$ {}'.format(ns))

elif f2 == True:
    d = 0.15 * s
    d = '{:.2f}'.format(d)
    d = str(d)
    d = d.replace('.',',')
    ns = 1.15 * s
    ns = '{:.2f}'.format(ns)
    ns = str(ns)
    ns = ns.replace('.', ',')
    s = '{:.2f}'.format(s)
    s = str(s)
    s = s.replace('.', ',')
    print('Seu antigo salário era de R$ {}'.format(s))
    print('Você recebeu um aumento de 15%')
    print('Você receberá R$ {} à mais'.format(d))
    print('Seu novo salário é de R$ {}'.format(ns))

elif f3 == True:
    d = 0.1 * s
    d = '{:.2f}'.format(d)
    d = str(d)
    d = d.replace('.', ',')
    ns = 1.1 * s
    ns = '{:.2f}'.format(ns)
    ns = str(ns)
    ns = ns.replace('.', ',')
    s = '{:.2f}'.format(s)
    s = str(s)
    s = s.replace('.', ',')
    print('Seu antigo salário era de R$ {}'.format(s))
    print('Você recebeu um aumento de 10%')
    print('Você receberá R$ {} à mais'.format(d))
    print('Seu novo salário é de R$ {}'.format(ns))


elif f4 == True:
    d = 0.05 * s
    d = '{:.2f}'.format(d)
    d = str(d)
    d = d.replace('.',',')
    ns = 1.05 * s
    ns = '{:.2f}'.format(ns)
    ns = str(ns)
    ns = ns.replace('.', ',')
    s = '{:.2f}'.format(s)
    s = str(s)
    s = s.replace('.', ',')
    print('Seu antigo salário era de R$ {}'.format(s))
    print('Você recebeu um aumento de 5%')
    print('Você receberá R$ {} à mais'.format(d))
    print('Seu novo salário é de R$ {}'.format(ns))
