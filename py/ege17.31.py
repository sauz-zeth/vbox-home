M = 1000
N = 9999
K = 5**5
s = 0
for i in range(N, M - 1, -1):
    if i >= K and (i % 25 == 11 or i % 25 == 13): 
        s += 1
        imin = i
print(s, imin)

