M = 1000
N = 70000
K8 = 8**4
L8 = 8**5
K5 = 5**5
L5 = 5**6
s = 0
imax = 0
for i in range(M, N + 1):
    f = L8 > i >= K8 and L5 > i >= K5 and i % 256 == 0xFA
    if f: 
        s += 1
        imax = i
print(s, imax)

