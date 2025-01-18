x = 8**511 - 4**511 + 2**511 - 511

n = 0
while x > 0:
    d = x % 2
    x = x // 2
    
    if d == 0:
        n += 1

print(n)
