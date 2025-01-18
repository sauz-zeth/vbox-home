def counter(a, n = 10000):
    c = [0] * n
    a = list(a)
    b = set(a)

    for x in a:
        if x in b:
            c[x] += 1

    return ((x, c[x]) for x in b)


a = [3, 1, 4, 3, 3, 2, 3, 4]
print(list(counter(a)))
