
from functools import cache
@cache
def f(n):
    if n <= 5:
        return n

    if n % 8 == 0:
        return n + f(n // 2 - 3)

    else:
        return n + f(n + 4)

for n in reversed(range(1, 10000)):
    try:
        f(n)
    except RecursionError:
        pass
    else:
        print(n)
        break
