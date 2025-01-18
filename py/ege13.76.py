x1 = 61
x2 = 59

for p in range(8, -1, -1):
    m = int('1' * p + '0' * (8 - p), 2)

    if x1 & m == x2 & m:
        print(m)
        break
