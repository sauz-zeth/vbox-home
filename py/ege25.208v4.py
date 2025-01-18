from math import inf
#12*45*

a = 0
b = 0
c = 0
i = 0
j = 0
k = 0
while a < 10 or b < 10 or c < 1 or i < 100 or j < 100 or k < 100:
    u = int(f"12{a}45") if a < 10 else inf
    v = int(f"1245{b}") if b < 10 else inf
    w = int(f"1245") if c < 1 else inf
    x = int(f"12{i:02d}45") if i < 100 else inf 
    y = int(f"1245{j:02d}") if j < 100 else inf
    z = int(f"12{k // 10}45{k % 10}") if k < 100 else inf

    m = min(u, v, w, x, y, z)

    if m % 51 == 0:
        print(m, m // 51)
    
    a += u == m
    b += v == m
    c += w == m
    i += x == m
    j += y == m
    k += z == m
