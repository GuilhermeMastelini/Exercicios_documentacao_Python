#Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será
# mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá
# uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na
# tela, informando se o usuário ganhou ou perdeu o jogo.

import random as rd

txt = []

with open('Lista_forca.txt','r') as lst:
    for i in lst:
        txt.append(i)



palavra = txt[rd.randrange(0,len(txt))]
palavra = palavra.upper()
print(palavra)

l = []

for i in palavra:
    l.append(i)

ll = []

for i in range(len(l)):
    rand = l[rd.randrange(0,len(l))]
    y = l.index(rand)
    ll.append(rand)
    l.remove(rand)


print(*ll)
ll = []
vidas = 6

print()

while vidas > 0:

    a = input('Palpite: ')
    a = a.upper()

    if a == palavra:
        print('Parabéns!!!')
        break

    vidas -= 1
    print(f'{vidas} vidas\n\n')

print()
print('#'*30)
print('GAME OVER')
print('#'*30)

