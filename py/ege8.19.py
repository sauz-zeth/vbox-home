from itertools import product

a = list(product('AMPT', repeat = 4))
print(''.join(a[250 - 1]))

