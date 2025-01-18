M = 8800
N = 55535
n = 1
s = 0
x = 0
imax = 0
for i in range(M, N + 1):
    x = i
    n = 1
    while x > 0:
        n = n * (x % 10)
        x //= 10
    if n > 35 and n % 7 == 0:
        imax = i
        s += 1
print(imax, s)
