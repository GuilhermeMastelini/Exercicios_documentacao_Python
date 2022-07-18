#
# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
#
# As possíveis respostas são:
#
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma
# . O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma das opções devem ser armazenados num vetor.
# Após os dados terem sido completamente informados, o programa deverá calcular
# a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800
#
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

print('Enquete')
print('1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro')

l =[]

while True:

    try:
        a = int(input('Vote aqui: '))
        if a == 0:
            break
        elif a >= 1 and a <= 6:
            l.append(a)

        else:
            print('Valor Inválido')
    except:
        print('Valor Inválido')


var_1 = l.count(1)
var_2 = l.count(2)
var_3 = l.count(3)
var_4 = l.count(4)
var_5 = l.count(5)
var_6 = l.count(6)

prct_1 = '{:.1f}'.format(var_1/len(l)*100)
prct_2 = '{:.1f}'.format(var_2/len(l)*100)
prct_3 = '{:.1f}'.format(var_3/len(l)*100)
prct_4 = '{:.1f}'.format(var_4/len(l)*100)
prct_5 = '{:.1f}'.format(var_5/len(l)*100)
prct_6 = '{:.1f}'.format(var_6/len(l)*100)

l_p = [prct_1,prct_2,prct_3,prct_4,prct_5,prct_6]

l_2 = [var_1,var_2,var_3,var_4,var_5,var_6]
vencedor_valor = max(l_2)
vencedor_indice = l_2.index(vencedor_valor)

l_3 = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro']


print('Sistema Operacional        Votos     %')
print('-------------------        -----     --')
print(f'Windows Server              {var_1:>2}       {prct_1:>2}%')
print(f'Unix                        {var_2:>2}       {prct_2:>2}%')
print(f'Linux                       {var_3:>2}       {prct_3:>2}%')
print(f'Netware                     {var_4:>2}       {prct_4:>2}%')
print(f'Mac OS                      {var_5:>2}       {prct_5:>2}%')
print(f'Outro                       {var_6:>2}       {prct_6:>2}%')
print('-------                   ------')
print(f'Total                       {len(l)}')



print(f'O Sistema Operacional mais votado foi o {l_3[vencedor_indice]}, com {vencedor_valor} votos, correspondendo a {max(l_p)}% dos votos')

