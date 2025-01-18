#сумма и кол-во собственных делителей числа
def divSumCountProper(x):
    s = 1
    j = 2
    k = 1
    while j * j < x:
        if x % j == 0:
            s += j + x // j
            k += 2
        j += 1 
    if j * j == x:
        s += j
        k += 1
    
    return s, k


N = 10000
for i in range (2, N + 1):
    s, k = divSumCountProper(i)
    if s == i:
        print(i, k)
        
