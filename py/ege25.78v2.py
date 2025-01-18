n = 0
N = 200000
for i in range(2, N + 1):
    prime = 1
    j = 2
    while j * j <= i:
        if i % j == 0:
            prime = 0
            break
        j += 1

    if prime:
        n += 1

print(n)
