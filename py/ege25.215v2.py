#2?1?2?1?2?1
from itertools import product

for p in product(range(2, -1, -1), repeat = 5):
    xs = "2%d1%d2%d1%d2%d1" % p
    
    x = int(xs, 3)
    if x % 148 == 0:
        print(x, x // 148)
