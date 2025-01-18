from math import sqrt
n = 0
M = 20000
for i in range(2, M + 1):
    prime = 1
    for x in range(2, int((sqrt(i)) + 1)):
        if i % x == 0:
            prime = 0
            break
    if prime:
        n += 1

print(n)

