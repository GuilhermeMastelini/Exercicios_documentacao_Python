# Calculadora de IMC
print('Claculadora de IMC')
a = int(input('Selecione (1) para Homem e (2) para Mulher '))
b = input('digite seu peso em Kg ')
c = input('digite sua altura em metros ')
b = b.strip()
c = c.strip()
b = b.replace(',','.')
c = c.replace(',','.')
b = float(b)
c = float(c)
imc = b/(c**2)
s = 'vazio'

if a == 1:
    s = 'O senhor'
elif a== 2:
    s = 'A senhora'

if imc <= 18.5:
    print ('{} está  baixo do peso.'.format(s))
elif imc > 18.5 and imc <= 24.9:
    print ('{} está com o peso normal'.format(s))
elif imc >= 25 and imc < 29.9:
    print ('{} está com pré obesidade'.format(s))
elif imc >= 30 and imc < 34.9:
    print ('{} está com obesidade'.format(s))
elif imc >= 35 and imc < 39.9:
    print ('{} está com obesidade grave'.format(s))
elif imc >= 40:
    print ('{} está com obesidade mórbida'.format(s))


