def limp(w):
    #recebe uma string e devolve um float
    w = w.strip()
    w = w.replace(',','.')
    w = float(w)
    return w

def f_s1(w):
    # recebe um float e devolve uma string com uma casa decimal
    w = '{:.1f}'.format(w)
    w = str(w)
    w = w.replace('.',',')
    return w

def f_s2(w):
    # recebe um float e devolve uma string com duas casas decimais
    w = '{:.2f}'.format(w)
    w = str(w)
    w = w.replace('.', ',')
    return w

def f_s3(w):
    # recebe um float e devolve uma string com três casas decimais
    w = '{:.3f}'.format(w)
    w = str(w)
    w = w.replace('.', ',')
    return w


def f_p(w):
    # recebe um float e devolve uma string com todas as casas decimais
    w = str(w)
    w = w.replace('.', ',')
    return w