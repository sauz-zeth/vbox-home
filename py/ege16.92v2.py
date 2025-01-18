f9 = False
f12 = False

def f(n):
    global f9
    global f12

    if n == 20 and f9 and f12:
        f9 = False
        f12 = False
        return 1

    if n > 20:
        f9 = False
        f12 = False
        return 0

    if n == 9:
        f9 = True
    if n == 12:
        f12 = True
    
    return f(n + 1) + f(n + 3) + f(n * 2)

f(3)
