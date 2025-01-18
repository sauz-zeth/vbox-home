from itertools import permutations

alpha = 'o' * 5 + 'e' * 7

summ = 0

for p in set(permutations(alpha)):
    s = ''.join(p)
    if 'oo' in s: continue
    
    if s[0] == 'o':
        summ += 4**12
    if s[0] == 'e':
        summ += 3 * 4**11

print(summ)
