def f(n):
    if n <= 3:
        return n
    else:
        if n % 2 == 0:
            return f(n-1) + 2 * f(n / 2)
        if n % 2 != 0:
            return f(n-1) + f(n-3)

for n in range(1, 10000):
    if f(n) >= 10**8:
        print(n)
        break
#65
