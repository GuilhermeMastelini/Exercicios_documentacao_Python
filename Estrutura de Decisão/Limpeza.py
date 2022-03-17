def limp(w):
    w = w.strip()
    w = w.replace(',','.')
    w = float(w)
    return w

def f_s1(w):
    w = '{:.1f}'.format(w)
    w = str(w)
    w = w.replace('.',',')
    return w

def f_s2(w):
    w = '{:.2f}'.format(w)
    w = str(w)
    w = w.replace('.', ',')
    return w

def f_s3(w):
    w = '{:.3f}'.format(w)
    w = str(w)
    w = w.replace('.', ',')
    return w


def f_p(w):
    w = str(w)
    w = w.replace('.', ',')
    return w