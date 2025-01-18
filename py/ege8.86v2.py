from itertools import product
from pprint import pprint
#ВЕКНО

i = 1
l = 0

for p in product('ВЕКНО', repeat = 5):
    if p.count('О') == 1 and p.count('Е') == 1:
        l = i
    
    i += 1

print(l)
