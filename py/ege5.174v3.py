a = set() 

def f(i):
    si = f"{i:b}"
    return si.replace('0', "")

for i in range(10, 2501):
    a.add(f(i))

print(len(a))

