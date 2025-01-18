x = 112
n = 96

for p in range(8 + 1):
    m = int('1' * p + '0' * (8 - p), 2)

    z = x & m == n
    if z:
        print(m)
