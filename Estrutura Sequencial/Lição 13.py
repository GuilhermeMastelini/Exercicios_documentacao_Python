#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.



#Bloco de entrada de números
a =input('Digite um número inteiro ')
b =input('Digite mais um número inteiro ')
c = input('Digite um número real ')

#Bloco de limpeza das variáveis (sprip para espaços e replace para substituir eventuais virgulas por pontos)
a = a.strip()
a = int(a)
b = b.strip()
b = int(b)
c = c.strip()
c = c.replace(',','.')
c = float(c)

#Bloco de cálculos e saida
p = (a*2)*(b/2)
s = (3*a) + c
k = c**3
print('Você escolheu os números {} , {} e {}'.format(a,b,c))
print('O produto do dobro de {} com metade de {} é igual à {}'.format(a,b,p))
print('A soma do triplo de {} com {} é igual à {}'. format(a,c,s))
print('{} elevado ao cubo é igual à {}'.format(c,k))
