#1*586?6
#2000000000

def dec2base(x, b):
    s = ''
    while x > 0:
        s = str(x % b) + s
        x = x // b

    return s

def f(x):
    sx = dec2base(x, 7)
    if sx == sx[::-1]:
        sa = map(int, sx)

        print(x, sum(sa))

#1586?6
for i in range(10):
    x = int(f"1586{i}6")
    f(x)

#1*586?6
for k in range(1, 5):
    for i1 in range(10 ** k):
        for i2 in range(10):
            x = int(f"1{i1:0{k}d}586{i2}6")
            f(x)

