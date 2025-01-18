x = (48 << 8) + 2
n = (48 << 8)

k = 0
for p in range(16 + 1):
    m = int('1' * p + '0' * (16 - p), 2)

    z = x & m == n
    if z:
        k += 1

print(k)
