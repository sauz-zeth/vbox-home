from functools import cache

#@cache
def f(n):
    if n < 3:
        return n + 1

    if n % 2 == 0:
#        return n + 2 * f(n + 2)
        return None
    else:
        return f(n - 2) + n - 2

k = 0
for n in range(1, 1000):
    fn = f(n)
    if fn is not None and 100 <= fn <= 999:
        k += 1

print(k)
