an = []

def f(n, k = 0):
    if k == 7:
        an.append(n)
        return 1
    if k > 7:
        return 0

    return f(n + 1, k + 1) + f(n + 5, k + 1) + f(n * 3, k + 1)

f(1)
print(len(set(an)))
