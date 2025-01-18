from math import inf
#12*45*

def f(x):    
    if x % 51 == 0:
        print(x, x // 51)

f(1245)

c = [0] * 5
x = [0] * 5

while c[0] < 10 or c[1] < 10 or c[2] < 100 or c[3] < 100 or c[4] < 100:
    x = [
        int(f"12{c[0]}45") if c[0] < 10 else inf,
        int(f"1245{c[1]}") if c[1] < 10 else inf,
        int(f"12{c[2]:02d}45") if c[2] < 100 else inf, 
        int(f"1245{c[3]:02d}") if c[3] < 100 else inf,
        int(f"12{c[4] // 10}45{c[4] % 10}") if c[4] < 100 else inf
    ]

    m = min(x)

    f(m)
    
    for i in range(len(c)):
        c[i] += x[i] == m
