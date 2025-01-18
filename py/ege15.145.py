def f(x, a):
    D34 = x % 34 == 0
    D51 = x % 51 == 0
    Da = x % a == 0

    return (D34 and not D51) <= (not Da or D51)

for a in range(1, 2000):
    if all(f(x, a) for x in range(1, 2000)):
        print(a)
        break
