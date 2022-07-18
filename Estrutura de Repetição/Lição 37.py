# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte
# a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de
# dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa
# também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e
# do mais magro, além da média das alturas e dos pesos dos clientes
print('Banco de Dados da academia\nDigite 0 para encerrar ')

lista_codigo = []
lista_altura = []
lista_peso = []
lista_altura_ordenada = []
lista_peso_ordenado = []


while True:
    continuar = input('Deseja continuar? ')
    if continuar == '0':
        break
    else:

        #Laço do código do cliente
        while True:

            try:
                codigo = input('Insira o código: ')
                if codigo == 0:
                    break
                else:
                    codigo = codigo.strip()
                    lista_codigo.append(codigo)
                    break
            except:
                print('Comando Inválido')

        #Laço da altura
        while True:

            try:
                altura = input('Insira a altura: ')
                if codigo == 0:
                    break
                else:
                    altura = altura.strip()
                    altura = altura.replace(',', '.')
                    altura = float(altura)
                    lista_altura.append(altura)
                    lista_altura_ordenada.append(altura)
                    break
            except:
                print('Comando Inválido')

        #Laço do peso
        while True:

            try:
                peso = input('Insira o peso: ')
                if codigo == 0:
                    break
                else:
                    peso = peso.strip()
                    peso = peso.replace(',','.')
                    peso = float(peso)
                    lista_peso.append(peso)
                    lista_peso_ordenado.append(peso)
                    break
            except:
                print('Comando Inválido')


lista_altura_ordenada.sort(reverse = True)
lista_peso_ordenado.sort(reverse = True)

mais_alto = lista_altura_ordenada[0]
mais_baixo = lista_altura_ordenada[-1]
mais_gordo = lista_peso_ordenado[0]
mais_magro = lista_peso_ordenado[-1]

index_mais_alto = lista_altura.index(mais_alto)
index_mais_baixo = lista_altura.index(mais_baixo)
index_mais_gordo = lista_peso.index(mais_gordo)
index_mais_magro = lista_peso.index(mais_magro)

print(f'O cliente mais alto é o cliente {lista_codigo[index_mais_alto]}')
print(f'O cliente mais baixo é o cliente {lista_codigo[index_mais_baixo]}')
print(f'O cliente mais gordo é o cliente {lista_codigo[index_mais_gordo]}')
print(f'O cliente mais magro é o cliente {lista_codigo[index_mais_magro]}')
