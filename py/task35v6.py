def counter(a):
    b = {} 

    for x in a:
        if x not in b:
            b[x] = 1
        else:
            b[x] += 1

    return b.items()


a = [3, 1, 4, 3, 3, 2, 3, 4]
print(list(counter(a)))
