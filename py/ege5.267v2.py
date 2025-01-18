def f(x):
    sx = f"{x:b}"

    l = sx[0]
    sx = sx[1:]

    sx = sx.replace('1', 'z')
    sx = sx.replace('0', '1')
    sx = sx.replace('z', '0')

    sx = l + sx

    return int(sx, 2) + x


for i in range(1, 100, 2):
    r = f(i)
    if r > 99:
        print(i)
        break
