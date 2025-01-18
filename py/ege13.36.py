#m = 240 * 256 + 0
m = 240 << 8

x = (150 << 8) + 18

#ipm = 2**16 - 1
ipm = (1 << 16) - 1

hm = ~m & ipm

k = x & hm

print(k)
