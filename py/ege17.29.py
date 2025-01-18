M = 2807
N = 8558
s = 0
imax = 0
for i in range(M, N + 1):
    if i % 4 == 3 and i % 9 == 5:
        s += i
        imax = i

print(imax, s)

    

