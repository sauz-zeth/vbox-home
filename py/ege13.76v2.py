x1 = (61 << 8) + 154
x2 = (59 << 8) + 137

for p in range(16, -1, -1):
    m = int('1' * p + '0' * (16 - p), 2)

    if x1 & m == x2 & m:
        print(m >> 8)
        break
