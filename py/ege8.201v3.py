n = 0

for x4 in range(1, 16):
    for x3 in range(x4, 16):
        for x2 in range(x3, 16):
            for x1 in range(x2, 16):
                for x0 in range(x1, 16):
                    n += 1

print(n)
