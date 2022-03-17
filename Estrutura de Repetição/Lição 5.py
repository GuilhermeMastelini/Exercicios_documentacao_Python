#Altere o programa anterior permitindo ao usuário informar as populações
# e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

programa = True

while programa == True:

    def limp(x):

        x = x.replace('.',' ')
        x = x.strip()
        x = x.replace(',','.')
        x = float(x)
        return x


    verpop = False
    t = 0
    ver_a = False
    ver_b = False
    txa = 0
    txb = 0

    while ver_a == False:
        a = input('Digite o número da população do país A: ')
        try:
            a = limp(a)
        except:
            print('Comando Invalido')
            a = 0

        if a > 0:
            ver_a = True

    while ver_b == False:
        b = input('Digite o número da população do país B: ')
        try:
            b = limp(b)
        except:
            print('Comando Invalido')
            b = 0

        if b > 0:
            ver_b = True

    def tx(w):
        verk = False
        while verk == False:
            w = input(f'Digite a taxa da população {w} em porcetagem\n Exemplo 15% digite: 0,15\n ')
            try:
                w = w.strip()
                w = w.replace(',','.')
                w = float(a)
                verk = True
            except:
                w = 0
            if w > 0 and w < 1:
                verk = True
            return w


    txa = tx(txa)
    txb = tx(txb)


    while verpop == False:

        pa = a*(1 + txa)**t
        pb = b*(1 + txb)**t
        ver = pa >= pb

        if ver == False:
            t = t + 0.1

        else:
            print(f'Serão nessessários {t:.2f} anos')
            verpop = True
    z = input('Deseja repetir o programa (s) (n)\n ')
    if z == 's':
        programa = True
    else:
        programa = False
