N = 2 * 2 * 3 * 7 * 2

#?6*6*?6

a = []

def f(x):
    if x % N == 0:
        a.append(x)

def divSum(x):
    j = 1
    s = 0
    while j * j < x:
        if x % j == 0:
            s += j + x // j
        
        j += 1
        
    if j * j == x:
        s += j

    return s 

#    if len(a) == 20:
#        for n in a:
#            print(n)
#        exit()

#?66?6
for i1 in range(1, 10):
    for i2 in range(10):
        x = int(f"{i1}66{i2}6")
        f(x)


#?6?6?6
for i1 in range(1, 10):
    for l1 in range(10):
        for i2 in range(10):
            x = int(f"{i1}6{l1}6{i2}6")
            f(x)

#?66??6
for i1 in range(1, 10):
    for l2 in range(10):
        for i2 in range(10):
            x = int(f"{i1}66{l2}{i2}6")
            f(x)

#?6?6??6
for i1 in range(1, 10):
    for l1 in range(10):
        for l2 in range(10):
            for i2 in range(10):
                x = int(f"{i1}6{l1}6{l2}{i2}6")
                f(x)
#
#
#for i1 in range(10):
#    for l1 in range(100):
#        for l2 in range(10):
#            for i2 in range(10):
#                x = int(f"{i1}6{l1:02d}6{l2}{i2}6")
#                f(x)
#
#for i1 in range(10):
#    for l1 in range(10):
#        for l2 in range(100):
#            for i2 in range(10):
#                x = int(f"{i1}6{l1}6{l2:02d}{i2}6")
#                f(x)

#print(len(a))

for x in sorted(set(a))[:7]:
    print(x, divSum(x))
