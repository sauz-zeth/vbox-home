#123*567?

#76543210

#1235670

#12305670

#123005670

N = 10**9

def f(y):
    for i in range(10):
        x = y + i
        if x % 169 == 0:
            print(x, x // 169)

f(1235670)

for i in range(10):
    f(int('123' + str(i) + '5670')) 


for i in range(10):
    for j in range(10):
        f(int('123' + str(i) + str(j) + '5670')) 


