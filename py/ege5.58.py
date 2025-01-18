for i in range(1000, 10000):
    x1, x2, x3, x4 = map(int, str(i))
    a = [x1 + x2, x3 + x4]

    z = str(max(a)) + str(min(a))

    if z == '1412':
        print(i)
        break
