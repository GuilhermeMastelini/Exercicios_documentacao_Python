#Os números primos possuem várias aplicações dentro da Computação,
# por exemplo na Criptografia. Um número primo é aquele que é divisível apenas
# por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é
# ou não um número primo.

l = []
lr = []

while True:
    try:
        a = int(input('Digite um número natural: '))
        if a > 0:
            break
    except:
        print('ERR0')


s = 0
for i in range(a):
    s += 1
    l.append(s)

c = 0
r = 1

for x in range(len(l)):
    r = a%l[x]

    if r == 0:
        c += 1

if (c > 2) or (c == 1):
    print(f'{a} não é um número primo')

else:
    print(f'{a} é um número primo')