#Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no
# qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
# 8  3  4
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima.
# Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado.
# Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

from itertools import permutations



m = []
l = []
p = permutations([1,2,3,4,5,6,7,8,9])

for i in p:
    l.append(i)

for i in range(len(l)):

    a = l[i][0] + l[i][1] + l[i][2]
    b = l[i][3] + l[i][4] + l[i][5]
    c = l[i][6] + l[i][7] + l[i][8]
    d = l[i][0] + l[i][3] + l[i][6]
    e = l[i][1] + l[i][4] + l[i][7]
    f = l[i][2] + l[i][5] + l[i][8]
    g = l[i][0] + l[i][4] + l[i][8]
    h = l[i][2] + l[i][4] + l[i][6]

    ver = a == b == c == d == e == f == g == h

    if ver == True:
        m.append(l[i])



for y in range(len(m)):
    print()

    print(f'{m[y][0]}{m[y][1]}{m[y][2]}')
    print(f'{m[y][3]}{m[y][4]}{m[y][5]}')
    print(f'{m[y][6]}{m[y][7]}{m[y][8]}')

    print()

print(f'{len(m)} quadrados magicos encontrados entre {len(l)} possíveis')