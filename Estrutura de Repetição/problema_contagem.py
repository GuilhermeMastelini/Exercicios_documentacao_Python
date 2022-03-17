
l1 = []
l2 = []

a = int(input('Dias de trabalho pessoa 1: '))
b = int(input('Folgas da pessoa 1: '))
c = int(input('Dias de trabalho pessoa 2: '))
d = int(input('Folgas da pessoa 2: '))
e = int(input('Dias corridos à comparar: '))

s = 0

while True:

    for i1 in range (a):
        if len(l1) >= e:
            break
        else:
            l1.append('t')

    for i2 in range (b):
        if len(l1) >= e:
            break
        else:
            l1.append('f')

    for i3 in range (c):
        if len(l2) >= e:
            break
        else:
            l2.append('t')

    for i4 in range (d):
        if len(l2) >= e:
            break
        else:
            l2.append('f')

    if (len(l1) or len(l2)) >= e:
        break

for x in range(e):

    if (l1[x] == 'f') and (l2[x] == 'f'):
        s = s +1
    else:
        s = s + 0


print(l1)
print()
print(l2)
print(f'{s} será o número de folgas coincidentes')