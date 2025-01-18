import math

s = 0

for i in range(6):
    a = [40] + [41] * 5
    a[i] = 1

    if i == 0:
        a[i + 1] = 20
    elif i == 1:
        a[i + 1] = 20
        a[i - 1] = 19
    elif i == 5:
        a[i - 1] = 20
    else:
        a[i - 1] = 20
        a[i + 1] = 20

    s += math.prod(a)

print(s)
