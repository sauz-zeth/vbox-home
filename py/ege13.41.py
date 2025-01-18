m = 192
n = 0

k = 0
for x in range(256):
    z = x & m == n
    if z:
        k += 1

print(k - 2)
