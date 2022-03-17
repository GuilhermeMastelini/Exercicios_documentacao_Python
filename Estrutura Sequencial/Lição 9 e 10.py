# 9 e 10Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
print('Conversor de temperatura')
e = int(input('Digite (1) para converter ºF para ºC \n                ou \nDigite (2) para converter ºC para ºF '))

if e == 1:
    a = float(input('Digite a temperatura em Fahrenheit '))
    b = ((a - 32) * (5 / 9))
    print ('A temperatura em Celcius é de {:.1f}º' .format(b))

elif e == 2:

    a = float(input('Digite a temperatura em Celcius '))
    b = (a*(9/5)+32)
    print('A temperatura em Fahrenheit é de {:.1f}º' .format(b))

else:
    print ('Comando Invalido')
