a = [0, 1, 2, 3]

for i in range(4, 100):
    if i % 2 == 0:
        f = a[i - 1] + 2 * a[i // 2]
    else:
        f = a[i - 1] + a[i - 3]

    a.append(f)

    if f >= 10**8:
        print(i - 1)
        break
