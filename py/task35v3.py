def counter(a, n = 10000):
    c = [0] * n
    b = []

    for x in a:
        c[x] += 1
        if c[x] == 1:
            b.append(x)

    return ((x, c[x]) for x in b)


a = [3, 1, 4, -2, 3, -2, 3, 4]
print(list(counter(a)))
