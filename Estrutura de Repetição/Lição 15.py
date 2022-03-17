#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

f1 = 0
f2 = 1

while True:
    try:
        n = int(input('Quantos termos você deseja gerar? '))
        if n > 0:
            break
        else:
            print('Digite um número inteiro positivo')

    except:
        print('Digite um número inteiro positivo')

for i in range(n):
    s = f1 + f2
    f1 = f2
    f2 = s

    print(s, end=' ')
