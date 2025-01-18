#12*45*

def f(x):    
    if x % 51 == 0:
        print(x, x // 51)

f(1245)


for i in range(10):
    x = int(f"12450{i}") 
    f(x)

for i in range(100):
    x = int(f"1245{i}") 
    f(x)

for i in range(10):
    x = int(f"120{i}45") 
    f(x)

for i in range(100):
    x = int(f"12{i}45") 
    f(x)

for i in range(10):
    for i2 in range(10):
        x = int(f"12{i}45{i2}") 
        f(x)


