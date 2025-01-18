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
    f(f"123{i:d}5670") 


for i in range(100):
    f(f"123{i:02d}5670") 


