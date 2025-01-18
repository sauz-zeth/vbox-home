def f(x):
    x1, x2, x3, x4 = map(int, str(x))
    a = [x1 + x2, x3 + x4]

    return str(max(a)) + str(min(a))


for i in range(1000, 10000):
    if f(i) == '1412':
        print(i)
        break
