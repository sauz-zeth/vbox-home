def f():
    for x in range(11):
        for y in range(11):
            l = int('702305', 25) + y * 25**4 + x * 25 + int('67090', 11) + y + x * 11**2
            if l % 131 == 0: return l
            
print(f() // 131)
