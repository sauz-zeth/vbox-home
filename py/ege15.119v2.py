def f(x, a1, a2):
    P = 25 <= x <= 51
    Q = 12 <= x <= 37
    A = a1 <= x <= a2

    return (P == Q) <= (not A)

arr = []
for a1 in range(100):
    for a2 in range(100):
        if all(f(k / 2, a1, a2) for k in range(200)):
            arr.append(a2 - a1)

print(max(arr))
