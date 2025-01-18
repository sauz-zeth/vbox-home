x1 = 178
x2 = 165


for p in range(8 + 1):
    m = int('1' * p + '0' * (8 - p), 2)

    if x1 & m != x2 & m:
        print(p + 3 * 8)
        break

