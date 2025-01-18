def f(x, a):
    Za = x & a == 0
    Z44 = x & 44 == 0
    Z76 = x & 76 == 0
    
    return (not Za) <= (Z44 <= (not Z76))

for a in reversed(range(1, 2000)):
    if all(f(x, a) for x in range(1, 2000)):
        print(a)
        break
