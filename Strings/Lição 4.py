#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
#
# F
# FU
# FUL
# FULA
# FULAN
# FULANO

a = input('Name: ')

l = []

for i in a:
    l.append(i)
    print(*l)

    