import sys
sys.setrecursionlimit(2000)

def f(n):
    if n == 1:
        return 1

    return f(n - 1) * n

print(f(1000))
