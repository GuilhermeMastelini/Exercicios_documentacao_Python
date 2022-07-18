#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no
# formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
print('Entrada vazia encerra o programa\n\n\n')

def Data(s):


    var = s.split('/')
    dia = str(var[0]).zfill(2)
    dia = int(dia)
    if dia > 31:
        erro_proposital
    mes = str(var[1]).zfill(2)
    mes = int(mes) -1
    ano = var[2]

    meses_ext = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

    print(dia,' de ', meses_ext[mes], ' de ', ano)


while True:

    try:
        a = input('Insira a data no formato DD/MM/AAAA: ')

        if a == '':
            break

        Data(a)

        print()

    except:
        print('Comando Inválido')
