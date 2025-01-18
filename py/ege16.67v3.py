from functools import cache

@cache
def f(n):
    if n < 3:
        raise Exception('my exception')
        return n + 1

    if n % 2 == 0:
        return n + 2 * f(n + 2)
    else:
        return f(n - 2) + n - 2

k = 0
for n in range(1, 1000):
    try:
        fn = f(n)
        if 100 <= fn <= 999:
            k += 1
    except RecursionError as err:
        print(err)
    except Exception as err:
        print(err)

print(k)
