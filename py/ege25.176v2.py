def factor(x, j = 2):
    if x < 2:
        return 0

    while j * j <= x:
        if x % j == 0:
            return j
        j += 2 if j > 2 else 1

    return x

def divMaxEvenOdd(x):
    emax = 0
    omax = 0
    j = 2
    while j <= x // 2:
        if x % j == 0:
            if j % 2 == 0:
                if j > emax:
                    emax = j
            else:
                if j > omax:
                    omax = j
            
        j += 1

    return emax, omax

def A(x):
    emax, omax = divMaxEvenOdd(x)

    if emax and omax:
        return abs(emax - omax)
    else:
        return 0
    

N = 5
n = 0
i = 250156

while n < N:
    i += 1

    a = A(i)
        
    if factor(a) == a and a % 10 == 9:
        print(i, a)
        n += 1



