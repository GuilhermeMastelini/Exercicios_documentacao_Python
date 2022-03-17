#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
# ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


ver = False

while ver == False:

    a = input('Cadastre de nome de usuário: ')
    b = input('Cadastre sua senha: ')

    if a == b:
        print('O nome não pode ser igual à senha\ntente novamente')
    else:
        print('Cadastro efetuado')
        ver = True
print('Fim')
