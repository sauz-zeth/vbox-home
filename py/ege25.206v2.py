# 1?34567?9
# 876543210
N = 9
for i in range(N + 1):
    for l in range(N + 1):
        x = 1 * 10**8 + i * 10**7 + 34567 * 10**2 + l * 10 + 9
        if x % 17 == 0:
            print(x, x // 17)

