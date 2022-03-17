#Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo,
# se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

a = input('Insira o 1º lado do triângulo: ')
b = input('Insira o 2º lado do triângulo: ')
c = input('Insira o 3º lado do triângulo: ')

a = a.replace(',','.')
b = b.replace(',','.')
c = c.replace(',','.')

a = float(a)
b = float(b)
c = float(c)


# Verificação de existência do triângulo

v1 = (a + b) > c
v2 = (a + c) > b
v3 = (b + c) > a

ver = v1 and v2 and v3

eq = (a == b) and (b == c) and (a == c)
iso = (a == b) or (b == c) or (a == c)
esc = (not eq) and (not iso)
print()
print('Três lados formam um triângulo quando \na soma de quaisquer dois lados for maior que o terceiro')
print()
if ver == True:
    if eq == True:
        print('Os lados {} , {} e {} definem um triângulo equilátero'.format(a,b,c))
    elif iso == True:
        print('Os lados {} , {} e {} definem um triângulo isósceles'.format(a, b, c))
    elif esc == True:
        print('Os lados {} , {} e {} definem um triângulo escaleno'.format(a, b, c))

else:
    print('Os lados {} , {} e {} não definem um triângulo.'.format(a,b,c))
