def f(n):
    return 255 - n

for n in range(0, 256):
    if f(n) - n == 45:
        print(n)
