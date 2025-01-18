def f(x, a1, a2):
    P = range(25, 51 + 1)
    Q = range(12, 37 + 1)
    A = range(a1, a2 + 1)

    fx = (x in P) == (x in Q)
    fy = not(x in A)

    return fx <= fy

arr = []

for a1 in range(100):
    for a2 in range(100):
        if all(f(x, a1, a2) for x in range(100)):
            arr.append(a2 + 1 - a1)

print(max(arr))
