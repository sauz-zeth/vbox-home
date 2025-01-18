from functools import cache

k = 0
@cache
def f(n):
    global k
    k += 1
    if n <= 3:
        k -= 1
        return n == 3
    
    if k == 1:
        s = f(n - 2)
    else:
        s = f(n - 1) + f(n - 2)

    k -= 1
    return s  

print(f(18))
