#Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita
# para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços
# e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

a = input('Entrada: ')

l = []

for i in a:
    if i != ' ':
        l.append(i)

#caso par

palindromo = 0

if (len(l) % 2) == 0:
    for i in range(int(len(l)/2)):
        if l[i] != l[(i+1) * (-1)]:
            palindromo +=1


#caso impar
else:
    for i in range(int(len(l) // 2)):
        if l[i] != l[(i+1) * (-1)]:
            palindromo +=1

print()
if palindromo == 0:
    print(f'{a} é um palíndromo')
else:
    print(f'{a} não é um palíndromo')