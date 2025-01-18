m = 0
pm = 0
while True:
    x = int(input())
    if x == 0: break

    if x > m:
        pm = m
        m = x
    elif pm < x < m:
        pm = x

print(m)
print(pm)
