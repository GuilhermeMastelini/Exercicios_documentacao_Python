# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
# fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar
# todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles,
# para verificar o que se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número
# indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# necessita da esfera;
# necessita de limpeza;
# a.necessita troca do cabo ou conector;
# a.quebrado ou inutilizado
# Uma identificação igual
# a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100
#
# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

print('1- necessita da esfera\n2- necessita de limpeza\n3- necessita troca do cabo ou conector\n4- quebrado ou inutilizado\n')

cod_1 = 0
cod_2 = 0
cod_3 = 0
cod_4 = 0

while True:
    try:

        codigo = int(input('Código do defeito: '))
        if codigo == 0:
            break
        elif codigo == 1:
            cod_1 += 1
        elif codigo == 2:
            cod_2 += 1
        elif codigo == 3:
            cod_3 += 1
        elif codigo == 4:
            cod_4 += 1
        else:
            print('Comando inválido')
    except:
        print('Comando Inválido')

soma = cod_1 + cod_2 + cod_3 + cod_4

per_1 = cod_1/soma * 100
per_2 = cod_2/soma * 100
per_3 = cod_3/soma * 100
per_4 = cod_4/soma * 100

def limp(x):
    x = '{:.2f}'.format(x)
    x = str(x)
    x = x.replace('.',',')
    x = x + '%'
    return(x)


with open('relatório_mouse.txt','w') as rlt:
    rlt.write('Situação                                  Quantidade         Percentual\n')

with open('relatório_mouse.txt','a') as rlt:
    rlt.write(f'{"1- necessita da esfera":<40} {cod_1:>8} {limp(per_1):>20}\n')

with open('relatório_mouse.txt','a') as rlt:
    rlt.write(f'{"2- necessita de limpeza":<40} {cod_2:>8} {limp(per_2):>20}\n')

with open('relatório_mouse.txt','a') as rlt:
    rlt.write(f'{"3- necessita troca do cabo ou conector":<40} {cod_3:>8} {limp(per_3):>20}\n')

with open('relatório_mouse.txt','a') as rlt:
    rlt.write(f'{"4- quebrado ou inutilizado":<40} {cod_4:>8} {limp(per_4):>20}\n')
