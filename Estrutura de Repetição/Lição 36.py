#Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado
# pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor
# #Montar a tabuada de: 5
#Começar por: 4
#Terminar em: 7

#Vou montar a tabuada de 5 começando em 4 e terminando em 7:
#5 X 4 = 20
#5 X 5 = 25
#5 X 6 = 30
#5 X 7 = 35
#Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

print('*'*20)
print('Tabuada')
print('*'*20)

while True:
    try:
        a = int(input('Insira o valor inicial: '))
        b = int(input('Insira o valor final: '))
        c = int(input('Qual número você deseja calcular: '))
        break
    except:
        print('ERR0')

for i in range(a,b+1,1):
    print(f'{c} x {i} = {c*(i)}')