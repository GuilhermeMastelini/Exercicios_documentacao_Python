# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no
# formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos
# verificadores edos caracteres de formatação.

l =[]


while True:

    a = input('Digite seu CPF no formato xxx.xxx.xxx-xx: ')

    for i in a:
        l.append(i)

    try:
        l[0] = int(l[0])
        l[1] = int(l[1])
        l[2] = int(l[2])
        l[4] = int(l[4])
        l[5] = int(l[5])
        l[6] = int(l[6])
        l[8] = int(l[8])
        l[9] = int(l[9])
        l[10] = int(l[10])
        l[12] = int(l[12])
        l[13] = int(l[13])


        if l[3] == '.' and l[7] == '.' and l[11] == '-':
            print('OK')
            break

    except:
        print('Formato Inválido')

