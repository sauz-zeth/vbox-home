from itertools import product, permutations

alpha = 'UDRL'
n = 0

for pp in product(product(alpha), permutations(alpha, 2), product(alpha)):
    print(sum(pp, ()))
    if pp[0][0] != 'U':
        n += 1

print(n)
