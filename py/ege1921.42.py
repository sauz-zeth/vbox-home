from functools import cache

N = 29
@cache
def f(n):
    if n > N:
        return 0

    a = [f(x) for x in [n + 2, n + 3, n * 2]]
    a_ = [x for x in a if x <= 0]

    return -max(a_) + 1 if a_ else -max(a)

#f(600)
for i in range(1, N * 2 + 1):
    print(i, f(i))
