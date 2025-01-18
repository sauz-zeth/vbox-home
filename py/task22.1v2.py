M = 2 * 10**9
s = 0
xmin = M
while True:
    x = int(input())
    if x == 0: break
    
    if x < xmin:
        xmin = x
        s = 1

    elif x == xmin:
        s += 1
print(s)
