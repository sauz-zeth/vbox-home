from itertools import product

alpha = 'ГГС'

def combCount(alpha):
    n = 0
    for p in product(alpha, repeat = 5):
        if p[0] == 'Г':
            n += 1
    return n


while True:
    if combCount(alpha) == 512:
        print(alpha.count('С'))
        break

    alpha += 'С'
    
