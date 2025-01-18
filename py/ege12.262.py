#s = '0' + '2' * 43 + '1' * 12 + '3' * 5 
s = '0' + '2' * 43 + '1' * 12 + '3' * 5

ss = s

while '01' in s or '02' in s or '03' in s:
    s = s.replace('01', '2302', 1)
    s = s.replace('02', '10', 1)
    s = s.replace('03', '201', 1)
    print(s)
print(s.count('1'))
print(s.count('2'))
print(s.count('3'))

#if ss.count('1') == 60 and ss.count('2') == 22 and ss.count('3') == 17:

print(ss.count('1'))

# 2 -> 1
# 1 -> 231
# 3 -> 2231

# n1 + n2 + n3 = 60 
# n1 + n3 = 17
# n2 = 60 - 17 = 43
# n3 = 17 - n1
# n3 * 2 + n1 = 22
# (17 - n1) * 2 + n1 = 22
# 34 - n1 = 22
# n1 = 12
# n3 = 5 

