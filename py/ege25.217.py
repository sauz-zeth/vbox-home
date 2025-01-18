#1*586?6
#2000000000

def dec2base(x, b):
    s = ''
    while x > 0:
        s = str(x % b) + s
        x = x // b

    return s

ddef f(x):
    sx = dec2base(x, 7)
    if sx == sx[::-1]:
        sa = map(int, sx)

        print(x, sum(sa))

#1586?6
for i in range(10):
    x = int(f"1586{i}6")
    f(x)


#1?586?6
for i1 in range(10):
    for i2 in range(10):
        x = int(f"1{i1}586{i2}6")
        f(x)

#1??586?6
for i1 in range(100):
    for i2 in range(10):
        x = int(f"1{i1:02d}586{i2}6")
        f(x)

#1???586?6
for i1 in range(1000):
    for i2 in range(10):
        x = int(f"1{i1:03d}586{i2}6")
        f(x)

#1????586?6
for i1 in range(10000):
    for i2 in range(10):
        x = int(f"1{i1:04d}586{i2}6")
        f(x)
