# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.


while True:
    try:
        t = int(input('Digite o número de turmas: '))
        break
    except:
        print('Comando Inválido')

s = 0
for i in range(t):
    while True:
        try:
            a = int(input(f'Digite o número de alunos da {i+1}º turma: '))
            if a < 41:
                s += a
                break
            else:
                print('A turma não pode passar de 40 alunos')
        except:
            print('Comando Inválido')

m = s/t
m = '{:.1f}'.format(m)

print(f'A média é de {m} alunos por turma')

