#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular
# o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

print('*******************************')
print('    Calculadora de Fatorial')
print('*******************************')

print('Para encerrar o programa digite x')
f = 1
l = []
while True:
    a = input('Digite o fatorial que deseja calcular: ')
    if (a == 'X' or a == 'x'):
        break
    try:
        a = int(a)
        if (a <= 16):
            for i in range(a):
                l.append(i + 1)
            for x in range(a):
                f1 = l[x]
                f = f1 * f
            print(f'O fatorial de {a} é  igual a {f}')
            l.clear()
            f = 1
            print('Para encerrar o programa digite x')
        else:
            print('Erro \nO programa só aceita números naturais até 16')
            print('Tente novamente. Para sair pressione x')
    except:
        print('Erro \nO programa só aceita números naturais até 16')
        print('Tente novamente. Para sair pressione x')

print('FIM')