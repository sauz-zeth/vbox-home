from itertools import product

BB = {2, 4, 6, 8, 10, 12}
CC = {3, 6, 9, 12, 15}

def f(x, a):
    A = x in a
    B = x in BB
    C = x in CC

    return B <= ((C and not A) <= (not B))

smin = 1000
for n in range(1, 7):
    for a in product(range(1, 20), repeat = n):
        if all(f(x, a) for x in range(1, 50)):
            s = sum(a)
            if s < smin:
                smin = s
    print(smin, n)

