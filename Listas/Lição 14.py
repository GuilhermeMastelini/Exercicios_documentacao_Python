# tilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

l = []

def func(a):
    while True:

        try:
            print()
            a = input('Digite (S) para sim ou (N) para não: ')
            a = a.strip()
            a = a.upper()

            if a == 'S':
                return (1)
                break
            elif a == 'N':
                return(0)
                break
            else:
                print('Comando Inválido')
        except:
            print('Comando Inválido')

print('Telefonou para a vítima?')
pergunta_1 = func('')
print('Esteve no local do crime?')
pergunta_2 = func('')
print('Mora perto da vítima?')
pergunta_3 = func('')
print('Devia para a vítima?')
pergunta_4 = func('')
print('Já trabalhou com a vítima?')
pergunta_5 = func('')

soma = pergunta_1 + pergunta_2 + pergunta_3 + pergunta_4 + pergunta_5

if soma < 2:
    print('Inoscente')

elif  2 == soma:
    print('Suspeito')

elif 3 <= soma <= 4:
    print('Cúmplice')

else:
    print('Assassino')






