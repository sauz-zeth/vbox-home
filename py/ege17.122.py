M = 1110
N = 1111101
s = 0
for i in range(N, M - 1, -1):
    if (i % 0o20 == 0 or i % 0x30 == 0) and \
        (i % 0b10 == 0 or i % 0b11 != 0 and \
        i % 0o22 != 0 and i % 0x3F != 0):
            imin = i
            s += 1
print(s, imin)
