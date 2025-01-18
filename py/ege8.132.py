def f(x, a):
    Da = x % a == 0
    D24 = x % 24 == 0
    D36 = x % 36 == 0

    return (not Da) <= ((not D24) and (not D36))

for a in range(100, 0, -1):
    if all(f(x, a) for x in range(1, 100)):
        print(a)
        break
