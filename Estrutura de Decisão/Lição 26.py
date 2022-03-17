#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool: até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina: até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da
# gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
import Limpeza

tipo = input('Escolha o tipo de combustível: \n (A) para álcool \n (G) para gasolina ')
tipo = tipo.strip()
tipo = tipo.upper()

litros = input('Digite quantos litros você pretende comprar: ')
litros = Limpeza.limp(litros)

if tipo == 'A':
    if litros < 20:
        preco = (litros * 1.9)*0.97
        desc = '3%'
    else:
        preco = (litros * 1.9)*0.95
        desc = '5%'

elif tipo == 'G':
    if litros < 20:
        preco = (litros * 2.5)*0.96
        desc = '4%'
    else:
        preco = (litros * 1.9)*0.94
        desc = '6%'
else:
    print('Erro')

preco = Limpeza.f_s2(preco)
print('Total a pagar R${} \nVocê recebeu um desconto de {}'.format(preco,desc))
