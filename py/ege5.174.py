a = [] 


for i in range(10, 2501):
    i1 = 1
    si = bin(i)

    n = si.count('1')

    for i in range(n - 1):
        i1 = i1 * 2 + 1

    a.append(i1)

print(len(set(a)))

