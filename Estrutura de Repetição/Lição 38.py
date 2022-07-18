# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o
# usuário digite o salário inicial do funcionário.

# entradada do salário inicial

def limpeza(x):
    try:
        x = x.strip()
        x = x.replace(',','.')
        x = float(x)
        return x
    except:
        print('Valor inválido')



while True:
    si = input('Digite o salário inicial: ')
    si = limpeza(si)
    break

#entrada do ano
while True:
    try:
        ano_consulta = int(input('Digite o ano de consulta: '))
        if ano_consulta >= 1996:
            break
    except:
        print('comando inválido')

#cálculo e apresentação dos dados

def apresenta(w):
    w = '{:.2f}'.format(w)
    w = str(w)
    w = w.replace('.',',')
    return w

if ano_consulta == 1996:
    si = apresenta(si)
    print(f'O sálarío é de RS{si}')

else:
    salario = si*(1+(0.015)*2**(ano_consulta-1997))
    salario = apresenta(salario)
    print(f'O sálarío é de RS{salario}')
