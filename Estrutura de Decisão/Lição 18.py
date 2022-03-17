#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print('Verificador de datas')

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês (valor numerico): '))
ano = int(input('Digite o ano: '))

mes30 = [4,6,9,11]
mes31 = [1,3,5,7,8,10,12]

ver30 = mes in mes30
ver31 = mes in mes31
verfev = (mes == 2)

# Verificação de bissexto
v1 = ano%4
v2 = ano%100
bv1 = (v1 == 0)
bv2 = (v2 == 0)
ver = bv1 or bv2

if ver30 == True:
    verdia = (dia >=1) and (dia <= 30)
    if verdia == True:
        print('A data {}/{}/{} é válida'.format(dia,mes,ano))
    else:
        print('A data {}/{}/{} não é válida'.format(dia, mes, ano))

elif ver31 == True:
    verdia = (dia >= 1) and (dia <= 31)
    if verdia == True:
        print('A data {}/{}/{} é válida'.format(dia,mes,ano))
    else:
        print('A data {}/{}/{} não é válida'.format(dia, mes, ano))

elif verfev == True:
    if ver == True:
        verdia = (dia >= 1) and (dia <= 29)
        if verdia == True:
            print('A data {}/{}/{} é válida'.format(dia,mes,ano))
        else:
            print('A data {}/{}/{} não é válida'.format(dia, mes, ano))
    else:
        verdia = (dia >= 1) and (dia <= 28)
        if verdia == True:
            print('A data {}/{}/{} é válida'.format(dia, mes, ano))
        else:
            print('A data {}/{}/{} não é válida'.format(dia, mes, ano))
else:
    print('A data {}/{}/{} não é válida'.format(dia, mes, ano))
