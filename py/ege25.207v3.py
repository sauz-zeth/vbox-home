#123*567?

#76543210

#1235670

#12305670

#123005670

N = 10**9

def f(y):
    for i in range(10):
        x = int(y) + i
        if x % 169 == 0:
            print(x, x // 169)

f(1235670)

for i in range(10):
    f("123%d5670" % i) 


for i in range(100):
    f("123%02d5670" % i) 


