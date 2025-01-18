d = {}

def F(n):
    if n not in d:
        d[n] = f(n)

    return d[n]

def f(n):
    if n <= 3:
        return n

    if n % 2 == 0:
        return F(n - 1) + 2 * F(n // 2)
    else:
        return F(n - 1) + F(n - 3)

for n in range(1, 100):
    if F(n) >= 10**8:
        print(n - 1)
        break
