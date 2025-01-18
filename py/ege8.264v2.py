from itertools import product

alpha = 'ГЕКЭ023'
digits = '023'

n = 0
for p in product(alpha, repeat = 4):
    n += 1

    if p[0] in digits and all(x + x not in ''.join(p) for x in alpha):
        print(n)
        print(p)
        break

 
