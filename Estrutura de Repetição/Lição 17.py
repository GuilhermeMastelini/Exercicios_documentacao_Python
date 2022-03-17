#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120

a = int(input('Digite: '))
l = []


for i in range (a):

    l.append(i+1)

l.sort(reverse = True)


t = len(l)
h = 1

for n in range(t):

    z = l[n] * h
    h = z


lx = [str(q) for q in l]
print(f'{a}! = ',' x '.join(lx),'=',h)
