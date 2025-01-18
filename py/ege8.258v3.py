from itertools import permutations
alpha = 'АИКЛМЬ'

def word2dec(w, alpha):
    x = 0
    d = dict(zip(alpha, range(len(alpha))))

    for c in w:
        x = x * len(alpha) + d[c]

    return x
    
for p in permutations(alpha, 6):
    if p[0] == 'К' and p[-1] == 'Ь':
        i = word2dec(p, alpha)
        ir = word2dec(reversed(p), alpha)
        
        if ir - i == 26655:
            print(p)
            print(sum(int(c) for c in str(i + 1)))
            break
