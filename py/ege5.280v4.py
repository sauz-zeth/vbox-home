def s1(i):
    return sum(int(d) for d in str(i) if int(d) % 2 != 0)

def s2(i):
    return sum(map(int, str(i)[::-2]))
    
#6080818
for i in range(6000000, 8181818):
    r = abs(s1(i) - s2(i))
    if r == 29:
        print(i)
        break

