# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
# respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idade = []
altura = []

for i in range(5):
    a = input('Digite a idade ')
    idade.append(a)
    b = input('Digite a altura ')
    altura.append(b)


def Inverte (x):
    a = []
    for i in range(len(x)):
        a.append(x[(i+1)*-1])
    return(a)

idade = Inverte(idade)
altura = Inverte(altura)

print(*idade, sep = '  ')
print(*altura, sep = '  ')

