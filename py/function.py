def ff(x):
    def f():
        nonlocal x
        print(x)
        x += 1

    return f

f1 = ff(1)
f2 = ff(2)
f1()
f1()
f1()
f2()

