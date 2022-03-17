#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

a = input('Dígite uma letra: ')

a = a.strip()
v1 = a.isalnum()
v2 = a.isalpha()
a = a.upper()
t = (a=='A') or (a =='E') or (a =='I') or (a =='O') or (a =='U')
w = len(a)
x = (w == 1)

if x == True:
    if v2 == True:

        if t == True:
            print('{} é uma vogal'.format(a))

        else:
            print('{} é uma consoante'.format(a))
    elif v1 == True:
        print('{} é um número'.format(a))


    else:
        print('{} é um simbolo especial'.format(a))

else:
    print('Esse programa só aceita um caracter por vez')
