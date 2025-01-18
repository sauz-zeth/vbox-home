def f(n):
    ns = bin(n)
    ns += ns[-1]
    ns += '0' if ns.count('1') % 2 == 0 else '1'
    ns += '0'
    return int(ns, 2)
    
n = 0

while True:
    n += 1
    r = f(n)
    if r > 114:
        print(r)
        break
