
l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



def encriptar(msg, chave):
    vector = []
    encript = []
    final = []
    for i in msg:
        i = i.lower()

        vector.append(i)

    for i in range(len(vector)):
        if vector[i] in l:
            for j in range(26):

                if j + chave < 26:
                    if vector[i] == l[j]:
                        encript.append(l[j - chave])


                else:
                    if vector[i] == l[j]:
                        encript.append(l[23 - j])
        else:
            encript.append(vector[i])





    return print(*encript)


def desencriptar(msg,chave):
    chave = -chave
    encriptar(msg,chave)


print('\nchaves de 1 à 26\n\n')
print('(1) para desencriptar\n(2) para encriptar\n')
a = input('Digite sua opção: ')


while True:

    try:

        if a == '1':
            mensagem = input('Digite a mensagem: ')
            print('\nchaves de 1 à 26\n\n')
            chave  = int(input('Digite a chave: '))
            desencriptar(mensagem,chave)
            break

        elif a == '2':
            mensagem = input('Digite a mensagem: ')
            print('\nchaves de 1 à 26\n\n')
            chave = int(input('Digite a chave: '))
            encriptar(mensagem,chave)
            break

        else:
            print('Comando Inválido')

    except:
        print('Comando Inválido')





