def counter(a):
    b = {} 

    for x in a:
        b.setdefault(x, 0)
        b[x] += 1

    return b.items()


a = [3, 1, 4, 3, 3, 2, 3, 4]
print(list(counter(a)))
