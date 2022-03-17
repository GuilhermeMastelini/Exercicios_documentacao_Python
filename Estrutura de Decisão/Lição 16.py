#Faça um programa que calcule as raízes de uma equação do segundo grau,
# na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências,
# informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero,
# a equação não é do segundo grau e o programa não deve fazer pedir
# os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais.
# Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

print('Calculadora de raizes de equações do 2º grau')
print('A equação de ter o formato ax2 + bx + c')
a = float(input('Insira o valor do coeficiente a: '))
b = float(input('Insira o valor do coeficiente b: '))
c = float(input('Insira o valor do coeficiente c: '))

delta = (b**2) - (4*a*c)
rd = delta**(1/2)


ver1 = (a == 0)
ver2 = (delta < 0)
ver3 = (delta == 0)

if ver1 == True:
    print('Não é uma equação do 2º grau')

else:
    if ver2 == True:
        print('Não existem raizes reais para essa equação')

    else:
        x1 = (-b + rd) / (2 * a)
        x2 = (-b - rd) / (2 * a)
        if ver3 == True:
            print('Existe apenas uma solução x = {}'.format(x1))
        else:
            print('As raízes são x1 = {} e x2 = {}'.format(x1,x2))
