#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
# taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um
# item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.


def somaImposto(t,c):

    p = c*(1+t/100)

    return(p)

while True:

    try:
        custo = input('Custo do produto: R$ ')
        custo = custo.replace(',','.')
        custo = float(custo)

        taxa = input('Insira a taxa em porcentagem: ')
        taxa = taxa.replace(',','.')
        taxa = float(taxa)

        preco = somaImposto(taxa,custo)
        preco = '{:.2f}'.format(preco)
        preco = preco.replace('.',',')
        print(preco)
        print()


    except:
        print('Comando Inválido')
