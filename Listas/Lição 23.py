# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
# Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
# e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o
# seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório,
# chamado "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso
#
# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%
#
# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
# de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá
# ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser
# feito através de uma função, que será chamada pelo programa principal.

lista =[]

with open('Teste Python.txt','r') as doc:
    info = doc.readlines()

for i in range(len(info)):
    info[i] = info[i].split()
    lista.append(info[i])

print(lista)

lista_nomes = []
lista_bits = []

for x in range(len(lista)):
    lista_nomes.append(lista[x][0])
    q = int(lista[x][1])
    lista_bits.append(q)

print(lista_nomes)
print(lista_bits)

lista_mb = []


for w in range(len(lista_bits)):
    a = lista_bits[w]
    a = float(a)
    a = a/(1024**2)
    a = '{:.2f}'.format(a)
    a = str(a)
    a = a.replace('.',',') + 'MB'
    lista_mb.append(a)

print(lista_mb)

soma = 0
for p in range(len(lista_bits)):
    soma += lista_bits[p]
print(soma)

lista_pecent =[]

for z in range(len(lista_bits)):
    per = lista_bits[z]/soma
    per = '{:.2f}'.format(per)
    per = str(per)
    per = per.replace('.',',') + '%'
    lista_pecent.append(per)

soma_ap = soma/(1024**2)
soma_ap = '{:.2f}'.format(soma_ap)
soma_ap = str(soma_ap)
soma_ap = soma_ap.replace('.',',') + 'MB'

media = soma/len(lista_bits)
media = media/(1024**2)
media = '{:.2f}'.format(media)
media = str(media)
media = media.replace('.',',') + 'MB'

print(lista_pecent)

with open('relatorio.txt','w') as relatorio:
    relatorio.write('Nº  Usuário         Espaço Utilizado        % em Uso\n')

with open('relatorio.txt','a') as relatorio:
    for ii in range(len(lista_bits)):
        relatorio.write(f'{ii+1}   {lista_nomes[ii]:<10}     {lista_mb[ii]:>16}        {lista_pecent[ii]:>7}   \n')
    relatorio.write(f'Espaço total ocupado {soma_ap} \n'+f'Espaço médio ocupado {media}')
