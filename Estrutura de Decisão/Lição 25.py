#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
# participação da pessoa no crime. Se a pessoa responder positivamente
# a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

s = 0
l = []
print('Responda as perguntas com SIM ou NÃO')

p1 = input('Telefonou para a vítima? ')
p2 = input('Esteve no local do crime? ')
p3 = input('Mora perto da vítima? ')
p4 = input('Devia para a vítima? ')
p5 = input('Já trabalhou com a vítima? ')

def limp(x):
    x = x.upper()
    x = x.strip()
    x = x.replace('Ã','A')
    return x

p1 = limp(p1)
p2 = limp(p2)
p3 = limp(p3)
p4 = limp(p4)
p5 = limp(p5)

l = [p1,p2,p2,p4,p5]

for i in range(5):
    if l[i] == 'SIM':
        s = s + 1
    else:
        s = s +0

if (s < 2):
    print('Inocente')
elif (s == 2):
    print('Suspeito')

elif (s == 3 or s == 4):
    print('Cúmplice')

elif (s == 5):
    print('Assassino')
else:
    print('Erro')
