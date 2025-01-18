def s1(i):
    s1 = 0

    for x in str(i):
        n = int(x)
        if n % 2 != 0:
            s1 += n

    return s1

def s2(i):
    s2 = 0
    si = str(i)
    
    if i % 2 != 0:
        se = si[::2]
    else:
        se = si[1::2]

    return sum(map(int, list(se)))
    

#for i in range(10000000, 20000000):
i = 1838581818
r = abs(s1(i) - s2(i))
print(r)
    if r == 29:
        print(i)

