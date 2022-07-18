# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro
# vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

l_1 = ['a','b','c','d','e','f','g','h','i','j']

l_2 = [1,2,3,4,5,6,7,8,9,10]

l = []

for i in range(10):
    l.append(l_1[i])
    l.append(l_2[i])

print(l)