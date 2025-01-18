def s1(i):
    s1 = 0

    while i > 0:
        d = i % 10
        if d % 2 != 0:
            s1 += d

        i //= 10

    return s1

def s2(i):
    s2 = 0
    si = str(i)
    
    se = si[::-2]

    return sum(map(int, se))
    

#6080818
for i in range(1, 8181818):
    r = abs(s1(i) - s2(i))
    if r == 29:
        print(i)
        break

