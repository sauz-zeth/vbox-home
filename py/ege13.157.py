m = 240
n = 176

x1 = (192 << 24) + (168 << 16) + (248 << 8)

x1c1 = x1.bit_count()
#x1c1 = f"{x1:b}".count('1')
x1c0 = 24 - x1c1

k = 0
for x in range(256):
    if n == m & x:
        if x1c1 + f"{x:b}".count('1') == x1c0 + f"{x:b}".count('0'):
            k += 1 

print(k)
