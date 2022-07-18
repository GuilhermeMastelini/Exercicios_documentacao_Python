# Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
#
# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!
#
# Digite uma letra: O
# A palavra é: _ _ _ _ O
#
# Digite uma letra: E
# A palavra é: _ E _ _ O
#
# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

vidas = 6

import random as rd

l_txt = []

palavra = ''

with open('Lista_forca.txt', 'r') as lt:
    for i in lt:
        l_txt.append(i)

palavra = l_txt[rd.randrange(0, len(l_txt))]
palavra = palavra.lower()
palavra = palavra.strip()
palavra = palavra.replace('é','e')
palavra = palavra.replace('ê','e')
palavra = palavra.replace('á','a')
palavra = palavra.replace('ã','a')
palavra = palavra.replace('ó','o')
palavra = palavra.replace('õ','o')
palavra = palavra.replace('í','i')
palavra = palavra.replace('ú','u')
palavra = palavra.upper()

l_palavra = []
l_jogo = []
print(f'Vidas: {vidas}')
print()

for i in palavra:
    l_palavra.append(i)
    l_jogo.append('_')

print(f'Palavra com {len(l_palavra)} letras')
print(*l_jogo)


while True:

    print()
    a = input('Palpite: ')
    a = a.upper()


    acerto = False

    for i in range(len(l_palavra)):

        if a == l_palavra[i]:
            l_jogo[i] = a
            acerto = True



    if acerto == False:
        vidas -=1
        print(f'Vidas: {vidas}')
        print()

    if vidas == 0:

        print('Game Over')
        print('A palavra era ',*l_palavra)
        break

    if '_' not in l_jogo:
        print(*l_palavra)
        print('Parabéns')
        break


    print()

    print(*l_jogo)

