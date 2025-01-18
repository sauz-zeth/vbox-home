m = 0
pm = 0
ppm = 0
while True:
    x = int(input())
    if x == 0: break

    if x > m:
        ppm = pm
        pm = m
        m = x

    elif pm < x < m:
        pm = x

    elif ppm < x <pm:
        ppm = x

print(m)
print(pm)
print(ppm)
