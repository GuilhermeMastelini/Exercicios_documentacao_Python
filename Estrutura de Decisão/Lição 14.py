#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre, e calcule a sua média.
# A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média,
# o conceito correspondente e a mensagem “APROVADO” se o
# conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

a = int(input('Digite o número de atividades: '))
s = 0
n = []

for i in range(1, a + 1):
    v = input('Digite a {}º nota: '.format(i))
    v = v.replace(',','.')
    v = float(v)
    n.append(v)
    s += v

m = s/a
ca = (m >= 9) and (m <= 10)
cb = (m < 9) and (m >= 7.5)
cc = (m < 7.5) and (m >= 6)
cd = (m < 6) and (m >= 4)
ce = (m < 4) and (m >= 0)


m = '{:.1f}'.format(m)

if ca == True:
    print('notas: {}'.format(n))
    print('Sua média final {}'.format(m))
    print('Conceito A')
    print('APROVADO')

elif cb == True:
    print('notas: {}'.format(n))
    print('Sua média final {}'.format(m))
    print('Conceito B')
    print('APROVADO')

elif cc == True:
    print('notas: {}'.format(n))
    print('Sua média final {}'.format(m))
    print('Conceito C')
    print('APROVADO')

elif cd == True:
    print('notas: {}'.format(n))
    print('Sua média final {}'.format(m))
    print('Conceito D')
    print('REPROVADO')

elif ce == True:
    print('notas: {}'.format(n))
    print('Sua média final {}'.format(m))
    print('Conceito D')
    print('REPROVADO')

else:
    print('ERRO')
