#сумма нетривиальных делителей числа
def divSum(x):
    global k
    s = 0
    j = 2
    while j * j < x:
        if x % j == 0:
            s += j + x // j
            k += 2
        j += 1 
    if j * j == x:
        s += j
        k += 1
    
    return s

    
def isPerfect(x):
    if x < 2:
        return False

    return divSum(x) + 1 == x


N = 10000
for i in range (2, N + 1):
    k = 1
    if isPerfect(i):
        print(i, k)
        
