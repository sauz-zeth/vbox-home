m = 0
pm = 0
ppm = 0
for i in range(3):
    x = int(input())
    if x >= m:
        ppm = pm
        pm = m
        m = x
    elif pm <= x < m:
        ppm = pm
        pm = x
    elif ppm <= x < pm:
        ppm = x
print(ppm, pm, m)
