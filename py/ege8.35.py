from pprint import pprint
from itertools import product

a = list(''.join(p) for p in product('ДКМО', repeat = 5))
n1 = a.index('ДОМОК') 
n2 = a.index('КОМОД')

print(n2 - n1 + 1)


