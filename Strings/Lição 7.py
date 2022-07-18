#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

a = input('Entrada: ')

vazio = 0
vogal = 0


for i in a:
    if i == ' ':
        vazio += 1
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vogal += 1

print()
print(f'{vazio} espaços em branco\n{vogal} vogais')
        