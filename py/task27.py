def factor(x, j = 2):
    if x < 2:
        return 0

    while j * j <= x:
        if x % j == 0:
            return j
        j += 2 if j > 2 else 1

    return x 

while True:
    i = int(input())
    a = 2
        
    while i > 1:
        a = factor(i, a)
        i = i // a
        print(a, end=" ")

    print()
