n = 0
N = 20000
for i in range(2, N + 1):
    prime = 1
    for x in range(2, i):
        if i % x == 0:
            prime = 0
            break
    if prime:
        n += 1

print(n)
