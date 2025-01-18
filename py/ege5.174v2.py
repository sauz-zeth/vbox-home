a = set() 

for i in range(10, 2501):
    si = bin(i)

    n = si.count('1')
    si1 = '1' * n

    a.add(si1)

print(len(a))

