def counter(a):
    b = []
    c = []

    for x in a:
        if x not in b:
            b.append(x)
            c.append(1)
        else:
            c[b.index(x)] += 1

    return zip(b, c)


a = [3, 1, 4, 3, 3, 2, 3, 4]
print(list(counter(a)))
