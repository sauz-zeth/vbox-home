from math import inf

f = open("ege18.2.txt")
T = [list(map(int, l.split())) for l in f if l != '\n']

def printt(T):
    for a in T:
        for x in a:
            print('%4.0f ' % x, end = '')
        print()

def sumMaxMin(m):
    E = 0 if m == max else inf

    T0 = [[0] + [E] * (len(T[0]) - 1)] + T
    A = [[E] + a for a in T0]
    k = len(A)
    n = len(A[0])
    printt(A)

    for i in range(1, k):
        for j in range(1, n):
            A[i][j] += m(A[i][j - 1], A[i - 1][j])

    return A[k - 1][n - 1]

print(sumMaxMin(max))
print(sumMaxMin(min))


