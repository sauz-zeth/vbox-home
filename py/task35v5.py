def counter(a, n = 10000):
    c = [0] * n
    b = set()

    for x in a:
        b.add(x)
        c[x] += 1

    return ((x, c[x]) for x in b)


a = [3, 1, 4, 3, 3, 2, 3, 4]
print(list(counter(a)))
