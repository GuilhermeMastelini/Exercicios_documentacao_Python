#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
# mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
 #       Salário Bruto: (5 * 220)        : R$ 1100,00
  #      (-) IR (5%)                     : R$   55,00
   #     (-) INSS ( 10%)                 : R$  110,00
    #    FGTS (11%)                      : R$  121,00
     #   Total de descontos              : R$  165,00
      #  Salário Liquido                 : R$  935,00

vh = input('Insira o valor da sua hora de trabalho: R$ ')
qh = input('Insira a quantidade de horas trabalhadas no mês: ')
vh = vh.strip()
vh = vh.replace(',','.')
vh = float(vh)
qh = qh.strip()
qh = qh.replace(',','.')
qh = float(qh)
sb = qh * vh
f1 = (sb < 900)
f2 = (sb >= 900) and (sb < 1500)
f3 = (sb >= 1500) and (sb < 2500)
f4 = (sb >= 2500)
sd = 0.03 * sb
fgts = 0.11 * sb
inss = 0.1 * sb

if f1 == True:
    ir = 0
    pir = '0'

elif f2 == True:
    ir = 0.05
    pir = '5'
elif f3 == True:
    ir = 0.1
    pir = '10'

elif f4 == True:
    ir = 0.15
    pir = '15'

sr = (ir*sb)
desc = sd + inss + sr
sl = sb - desc

sb = '{:.2f}'.format(sb)
sb = str(sb)
sb = sb.replace('.',',')

sd = '{:.2f}'.format(sd)
sd = str(sd)
sd = sd.replace('.',',')

inss = '{:.2f}'.format(inss)
inss = str(inss)
inss = inss.replace('.',',')

fgts = '{:.2f}'.format(fgts)
fgts = str(fgts)
fgts = fgts.replace('.',',')

sr = '{:.2f}'.format(sr)
sr = str(sr)
sr = sr.replace('.',',')

desc = '{:.2f}'.format(desc)
desc = str(desc)
desc = desc.replace('.',',')

sl = '{:.2f}'.format(sl)
sl = str(sl)
sl = sl.replace('.',',')


print('Holerite \n \n ')
print('Salario Bruto R$ {}'.format(sb))
print('Descontos: \n ')
print('(-) INSS (10%) R$ {}'.format(inss))
print('(+) FGTS (11%) R$ {}'.format(fgts))
print('(-) IR ({}%) R$ {}'.format(pir,sr))
print('Total de Descontos R$ {}'.format(desc))
print('Salario Líquido à receber R$ {}'.format(sl))
