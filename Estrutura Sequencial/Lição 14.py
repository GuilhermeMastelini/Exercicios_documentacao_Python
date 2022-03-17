#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

print('Calculadora de Salário')
a = input('Qual é o valor da sua hora de trabalho? ')
b = input('Quantas horas você trabalha por mês? ')
a = a.strip()
a = a.replace(',','.')
a = float(a)
b = b.strip()
b = int(b)
salario_bruto = a*b
inss  = salario_bruto * 0.08
ir  = salario_bruto * 0.11
sdct = salario_bruto * 0.05
salario_liquido = salario_bruto - inss - ir - sdct

salario_bruto = '{:.2f}'.format(salario_bruto)
salario_bruto = str(salario_bruto)
salario_bruto = salario_bruto.replace('.',',')

inss = '{:.2f}'.format(inss)
inss = str(inss)
inss = inss.replace('.',',')

ir = '{:.2f}'.format(ir)
ir = str(ir)
ir = ir.replace('.',',')

sdct = '{:.2f}'.format(sdct)
sdct = str(sdct)
sdct = sdct.replace('.',',')

salario_liquido = '{:.2f}'.format(salario_liquido)
salario_liquido = str(salario_liquido)
salario_liquido = salario_liquido.replace('.',',')


print('Seu salário bruto é de R$ {}'.format(salario_bruto))
print('Desconto do INSS R$ -{}'.format(inss))
print('Desconto do IR R$ -{}'.format(ir))
print('Desconto do sindicato R$ -{}'.format(sdct))
print('Seu salário líquido à receber é R${}'.format(salario_liquido))
