#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados,
# obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você
# fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número
# novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

import random as rd

def parDados():

     d1 = rd.randrange(1,13)
     d2 = rd.randrange(1,13)
     soma = d1 + d2
     return(d1,d2,soma)

end = 0

while end == 0:

    a = input('Jogar dados ')
    a = parDados()
    print(f'Dado_a {a[0]}   Dado_b {a[1]}     Soma {a[2]}')

    if a[2] == 7 or a [2] == 11:
        print()
        print('Natural! Você venceu!')
        break

    elif a[2] == 2 or a[2] == 3 or a[2] == 12:
        print()
        print('Craps! Você perdeu!')
        break
    else:
        pronto = a[2]
        print(f'{pronto} é seu ponto!')
        print()

        while True:
            a = input('Jogar dados ')
            a = parDados()
            print(f'Dado_a {a[0]}   Dado_b {a[1]}     Soma {a[2]}')
            print()


            if a[2] == pronto:
                print('Ponto! Você venceu!')
                end = 1
                break


            elif a[2] == 7:
                print('7! Você perdeu!')
                end = 1
                break
