import Limpeza

a = input('Digite o primeiro valor: ')
b = input('Digite o segundo valor:  ')

a = Limpeza.limp(a)
b = Limpeza.limp(b)

c = a+b

c = Limpeza.f_s2(c)

print('A soma é {}'.format(c))
