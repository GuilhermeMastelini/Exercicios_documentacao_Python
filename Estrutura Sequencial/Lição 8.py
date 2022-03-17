# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

a = float(input('Digite o valor da sua hora-aula '))
b = int(input('Digite a quantidade de aulas semanais '))

c = (a*b)*4.5

print('Seu salário médio é de {:.2f}'.format(c))
