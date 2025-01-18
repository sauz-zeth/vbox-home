from itertools import product
from pprint import pprint
#ВЕКНО

i = int('44444', 5) + 1

for p in product('ОНКЕВ', repeat = 5):
    if p.count('О') == 1 and p.count('Е') == 1:
        print(i)
        break
    
    i -= 1

