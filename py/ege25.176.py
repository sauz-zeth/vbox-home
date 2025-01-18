def factor(x, j = 2):
    if x < 2:
        return 0

    while j * j <= x:
        if x % j == 0:
            return j
        j += 2 if j > 2 else 1

    return x

def filterEvenOdd(x, p):
    return x * (x % 2 == p)

feo = filterEvenOdd

def maxEvenOdd(a, b, p):
    return max(feo(a, p), feo(b, p))

def divMaxEvenOdd(x):
    emax = 0
    omax = 0
    j = 2
    while j * j <= x:
        if x % j == 0:
            j1 = x // j

            em = maxEvenOdd(j, j1, 0)
            om = maxEvenOdd(j, j1, 1)

            if em > emax:
                emax = em
            if om > omax:
                omax = om
            
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



