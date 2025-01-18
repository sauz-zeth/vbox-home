#123*OE56
#100000000

def f(x):
    if x % 206 == 0:
        print(x, x // 206)


#123OE56
for o in range(1, 10, 2):
    for e in range(0, 10, 2):
        x = int(f"123{o}{e}56")
        f(x)

#123?OE56
for i in range(10):
    for o in range(1, 10, 2):
        for e in range(0, 10, 2):
            x = int(f"123{i}{o}{e}56")
            f(x)


