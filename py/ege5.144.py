def f(x):
    xs = bin(x)
    xs += '00' if x % 2 == 0 else '11'

    return int(xs, 2)
    
n = 0

while True:
    n += 1
    if f(n) > 115:
        print(n)
        break
