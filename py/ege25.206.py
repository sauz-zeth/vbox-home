N = 9
for i in range(N + 1):
    for l in range(N + 1):
        x = int('1' + str(i) + '34567' + str(l) + '9')
        if x % 17 == 0:
            print(x, x // 17)

