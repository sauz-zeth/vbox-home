N = 21
a = 0
b = 1
print("%10d" % a)
print("%10d" % b)
for i in range(2, N + 1):
    c = a + b
    a = b
    b = c
    print("%10d" % c)

