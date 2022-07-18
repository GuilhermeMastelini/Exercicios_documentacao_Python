# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
#
# FULANO
# FULAN
# FULA
# FUL
# FU
# F

a = input('Type your name: ')

for i in range(len(a)):
    print(a)
    a = a[:-1]
