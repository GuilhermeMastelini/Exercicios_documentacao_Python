# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('Calculadora de médias')
b1 = int(input('Digite aqui a nota do 1º bimestre: '))
b2 = int(input('Digite aqui a nota do 2º bimestre: '))
b3 = int(input('Digite aqui a nota do 3º bimestre: '))
b4 = int(input('Digite aqui a nota do 4º bimestre: '))

if (b1 >= 0 and b1 < 11) and (b2 >= 0 and b2 < 11) and (b3 >= 0 and b3 < 11) and (b4 >= 0 and b4 < 11):
    m = (b1 + b2 + b3 + b4)/4
    print ('A média final é {}'.format(m))
else:
    print('nota inválida')
