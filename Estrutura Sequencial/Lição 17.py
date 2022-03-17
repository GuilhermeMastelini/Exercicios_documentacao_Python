#Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

import math
a = input('Digite o tamanho do arquivo em MB: ')
b = input('Digite a velocide do link em Mbps: ')
a = a.strip()
a = a.replace(',','.')
a = float(a)
b = b.strip()
b = b.replace(',','.')
b = float(b)
b = b/8
c = (b/a)/60
c = math.ceil(c)
print('Seu download vai demorar aproximadamente {} minutos'.format(c))
