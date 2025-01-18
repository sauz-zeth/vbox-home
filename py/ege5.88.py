def bitodd(nb):
    if nb.count('1') % 2 == 0:
        return '0'
    else:
        return '1'

def f(x):
    nb = bin(x)
    nb += bitodd(nb)
    nb += bitodd(nb)
    return int(nb, 2)
    
n = 0

while True:
    n += 1
    if f(n) > 103:
        print(n)
        break
