y = f'{0xb72:b}'
print(y)

a = ['ABDBCA', 'DABCA', 'DDBCA', 'ABCDA']
n = 0

for x in a:
    n += 1
    x = x.replace('A', '10')
    x = x.replace('B', '11')
    x = x.replace('C', '100')
    x = x.replace('D', '101')
    
    if x == y: print(n)
