d = {}

def f(n):
    if n in d:
        return d[n]

    if n <= 3:
        return n

    if n % 2 == 0:
        d[n] = f(n - 1) + 2 * f(n // 2)
        return d[n]
    else:
        d[n] = f(n - 1) + f(n - 3)
        return d[n]

for n in range(1, 100):
    if f(n) >= 10**8:
        print(n - 1)
        break
