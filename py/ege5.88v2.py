def f(x):
    nb = bin(x)
    nb += '1' if nb.count('1') % 2 != 0 else '0' 
    nb += '0'
    return int(nb, 2)
    
n = 0

while True:
    n += 1
    if f(n) > 103:
        print(n)
        break
