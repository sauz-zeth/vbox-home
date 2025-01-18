s = '8' * 9 + '5' * 12

while '555' in s or '888' in s:
    s = s.replace('555', '8')
    s = s.replace('888', '5')

print(s)

