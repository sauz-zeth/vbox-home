def f(i):
    si = ''.join(reversed(f"{i:b}"))

    return int(si, 2)

for i in range(500, 0, -1):
    if f(i) == 11:
        print(i)
        break
