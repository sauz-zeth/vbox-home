n = int(input())
a = 0
b = 0
c = 1

print("%10d" % a)

if n > 0:
    print("%10d" % b)

if n > 1:
    print("%10d" % c)

for i in range(3, n + 1):
    d = a + b + c
    a = b
    b = c
    c = d
    print("%10d" % d)

