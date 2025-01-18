def f(x, a):
    Z = lambda m: x & m == 0
    
    return (not Z(a)) <= (Z(44) <= (not Z(76)))

for a in reversed(range(1, 2000)):
    if all(f(x, a) for x in range(1, 2000)): break

print(a)
