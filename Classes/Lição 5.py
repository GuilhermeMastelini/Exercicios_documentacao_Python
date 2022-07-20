#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes
# atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome,
# depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

import random as rd



class Conta():

    def __init__(self,numero,nome,saldo):
        self.numero = numero
        self.nome = nome

        if saldo == '':
            self.saldo = 0
        else:
            self.saldo = float(saldo)

        print(self.nome)
        print(f'Número da conta {self.numero}\nSaldo: {self.saldo}\n\n')

    def Altera(self,novo_nome):
        self.nome = novo_nome
        print(f'Número da conta {self.numero}\nSaldo: {self.saldo}\n\n')

    def Saque(self,saq):

        self.saldo -= saq
        print(f'Número da conta {self.numero}\nSaldo: {self.saldo}\n\n')

    def Deposito(self,dep):
        self.saldo += dep
        print(f'Número da conta {self.numero}\nSaldo: {self.saldo}\n\n')



nome = input('Nome: ')
numero = rd.randrange(1000,9999,1)
saldo = input('Deposito inicial: ')

c1 = Conta(numero,nome,saldo)

while True:

    print()
    print('(1)Depósito\n(2)Saque\n(3)Alteração de Nome\n\n')
    x = input(': ')

    if x == '1':
        dep = float(input('Valor: '))
        c1.Deposito(dep)

    elif x == '2':
        saq = float(input('Valor: '))
        c1.Saque(saq)

    elif x == '3':
        novo = input('Novo nome: ')
        c1.Altera(novo)

    else:
        print('Comando Inválido\n')

