#Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.


a = input('Digite a primeira nota: ')
b = input('Digite a segunda nota: ')
a = a.strip()
b = b.strip()
a = a.replace(',','.')
b = b.replace(',','.')
a = float(a)
b = float(b)
media = (a+b)/2
v1 = (media >= 7) and (media < 10)
v2 = (media < 7)
v3 = (media == 10)

if v1 == True:
    media = '{:.1f}'.format(media)
    media = str(media)
    media = media.replace('.', ',')
    print('Aprovado com média {}'.format(media))

elif v2 == True:
    media = '{:.1f}'.format(media)
    media = str(media)
    media = media.replace('.', ',')
    print('Reprovado com média {}'.format(media))

elif v3 == True:
    print('Aprovado com Distinção')

else:
    print('Erro. Verifique as notas digitadas e tente novamente')
    print(media)
