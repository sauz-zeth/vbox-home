from itertools import product

i = 0
for p in product('AMPT', repeat = 4):
    if i == 250 - 1:
        print(''.join(p))

    i += 1

