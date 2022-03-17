#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
# inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
# A saída deve ser conforme o exemplo abaixo:

while True:
    a = input('Digite o valor da tabuada desejada: ')
    a = a.strip()
    a = a.replace(',','.')
    try:
        a = float(a)
        break
    except:
        print('O programa só executa números')
        print('Tente novamente')


for i in range(1,11,1):
    print(f'{i} x {a} = {a*i}')
