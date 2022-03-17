# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
x = False

while x == False:
    a = input('Selecione o turno que você estuda: \n \n (M) para matutino \n (V) para Vespertino \n (N) para noturno ')
    a = a.upper()
    a = a.strip()

    if a == 'M':
        print('Bom Dia!')
        x = True

    elif a == 'V':
        print('Boa Tarde!')
        x = True

    elif a == 'N':
        print('Boa Noite!')
        x = True

    else:
        print('Comando inválido \n \nTente novamente \n ')
