x = 112
n = 96

for p in range(8 + 1):
    m = 2 ** 8 - 2 ** (8 - p)

    z = x & m == n
    if z:
        print(m)
