#Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as
# conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário
# repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def Converte(h,m):

    if h > 12:
        h = h - 12

        return(f'{str(h).zfill(2)}:{str(m).zfill(2)} P.M.')

    else:
        return(f'{str(h).zfill(2)}:{str(m).zfill(2)} A.M.')

while True:
    try:
        hora = int(input('Horas: '))
        min = int(input('Minutos: '))

        x = Converte(hora,min)
        print(x)
        print()

    except:
        print('Comando Inválido')


