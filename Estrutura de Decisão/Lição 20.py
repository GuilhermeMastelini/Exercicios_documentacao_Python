#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular
# a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

q = int(input('Quantas notas serão inseridas: '))
s = 0
l = []

for i in range(q):

    a = input('Digite a {}º nota: '.format(i+1))
    a = a.strip()
    a = a.replace(',','.')
    a = float(a)
    l.append(a)

print('As notas foram: {}'.format(l))


for i2 in range(len(l)):
    s = s + l[i2]

media = s/(len(l))

apr = (media >= 7) and (media < 10)
aprL = (media == 10)
repr = (media < 7) and (media >=0 )

media = '{:.1f}'.format(media)
media_limpa = str(media)
media_limpa = media_limpa.replace('.',',')

if aprL == True:
    print('Aprovado com Louvor, média 10')

elif apr == True:
    print('Aprovado com média {}'.format(media_limpa))

elif repr == True:
    print('Reprovado com média {}'.format(media_limpa))

else:
    print('ERRO')
