from itertools import product
from pprint import pprint

i = 1
for p in product('ИОУ', repeat = 5):
    if i == 240:
        x = "".join(p)
        print(x)
        break
    
    i += 1

