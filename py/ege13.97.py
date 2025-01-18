x = 200
n = 192


for p in range(8 + 1, -1, -1):
    m = int('1' * p + '0' * (8 - p), 2)
    z = x & m == n

    if z:
        print(f"{m:b}".count('0') + 8)
        break
