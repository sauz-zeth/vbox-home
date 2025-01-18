def f(x, a):
    D15 = x % 15 == 0
    D18 = x % 18 == 0
    DA = x % a == 0

    return (DA and not D15) <= (D18 or D15)

for a in range(1, 500):
    if all(f(x, a) for x in range(500)):
        print(a)
        break
