# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

a = input('Digite (M) para masculino \n Digite (F) para feminino')
a = a.upper()
a = a.strip()

if a == 'M':
    print('Sexo Masculino selecionado.')
elif a == 'F':
    print('Sexo Feminino selecionado.')
else:
    print('Comando Inválido')
