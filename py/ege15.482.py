def f(x, a1, a2):
    P = 10 <= x <= 40
    Q = 5 <= x <= 15
    R = 35 <= x <= 50
    A = a1 <= x <= a2

    return (P <= Q) or ((not A) <= R)

arr = []
for a1 in range(100):
    for a2 in range(100):
        if all(f(k / 2, a1, a2) for k in range(200)):
            arr.append(a2 - a1)

print(min(arr))
