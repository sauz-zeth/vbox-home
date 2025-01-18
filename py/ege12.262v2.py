def f(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '2302', 1)
        s = s.replace('02', '10', 1)
        s = s.replace('03', '201', 1)
#        print(s)
    return(s)

for n1 in range(61):
    for n2 in range(61 - n1):
        for n3 in range(61 - n1 - n2):
            s = '0' + '1' * n1 + '2' * n2 + '3' * n3
            ss = f(s)
            if ss.count('1') == 60 and ss.count('2') == 22 and ss.count('3') == 17:
                print(n1)

# 2 -> 1
# 1 -> 231
# 3 -> 2231

# n1 + n2 + n3 = 60 

