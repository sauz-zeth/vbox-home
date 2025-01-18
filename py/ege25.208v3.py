from math import inf
#12*45*

def f(x):    
    if x % 51 == 0:
        print(x, x // 51)

f(1245)

i = 0
j = 0
while i < 10 or j < 10:
    x = int(f"12{i}45") if i < 10 else inf
    y = int(f"1245{j}") if j < 10 else inf
    m = min(x, y)

    f(m)

    i += x == m 
    j += y == m


i = 0
j = 0
k = 0
while i < 100 or j < 100 or k < 100:
    x = int(f"12{i:02d}45") if i < 100 else inf 
    y = int(f"1245{j:02d}") if j < 100 else inf
    z = int(f"12{k // 10}45{k % 10}") if k < 100 else inf
    m = min(x, y, z)

    f(m)

    i += x == m
    j += y == m
    k += z == m
