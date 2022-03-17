#Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido

a = int(input('Digite um número relacionado ao dia da semana: '))
b = a-1
semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
c = (a>=1) and (a<8)

if c == True:
    print(semana[b])
else:
    print('Valor Inválido')
