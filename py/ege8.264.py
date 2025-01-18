from itertools import product
alpha = 'ГЕКЭ023'

letters = 'ГЕКЭ'

n = 0
    
for p in product(alpha, repeat = 4):
    n += 1

    if any(p[0] == x for x in letters): continue
    if any(x + x in ''.join(p) for x in alpha): continue


    print(n)
    break

 
