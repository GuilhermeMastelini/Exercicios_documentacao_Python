#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
 #                     Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos
# tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de
# 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
# pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
import Limpeza

produto = input('Escolha o produto:\n (1) File Duplo \n (2) Alcatra \n (3) Picanha ')
kilos = input('Quantos quilos? ')
pagamento = input('Escolha a forma de pagamento:\n (1) Dinheiro \n (2) Cartão ')
kilos = Limpeza.limp(kilos)

if produto == '1':
    tipo = 'File Duplo'
    if kilos < 5:
        preco = 4.9*kilos
    else:
        preco = 5.8*kilos

elif produto == '2':
    tipo = 'Alcatra'
    if kilos < 5:
        preco = 5.9*kilos

    else:
        preco = 6.8*kilos

elif produto == '3':
    tipo = 'Picanha'
    if kilos < 5:
        preco = 6.9
    else:
        preco = 7.8

else:
    print('Produto não cadastrado')
    quit()

kilos = Limpeza.f_s3(kilos)


if pagamento == '2':
    precod = preco*0.95
    preco = Limpeza.f_s2(preco)
    precod = Limpeza.f_s2(precod)
    print('{} Kg de {}\n Total R$ {} \n Você ganhou 5% de Desconto \n Total a pagar R$ {}'.format(kilos,tipo,preco,precod))

else:

    preco = Limpeza.f_s2(preco)
    print('{} Kg de {}\n Total a pagar R$ {}'.format(kilos, tipo, preco))
