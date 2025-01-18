from itertools import permutations
alpha = 'АИКЛМЬ'

def word2dec(w, alpha):
    x = 0
    for c in w:
        x = x * len(alpha) + alpha.index(c)

    return x
    
for p in permutations(alpha, 6):
    if p[0] == 'К' and p[-1] == 'Ь':
        i = word2dec(p, alpha)
        ir = word2dec(reversed(p), alpha)
        
        if ir - i == 26655:
            print(sum(int(c) for c in str(i + 1)))
            break
