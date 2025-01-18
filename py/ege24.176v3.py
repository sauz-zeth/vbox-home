f = open('ege24.176.txt')

s = f.readline().strip()

s = s.replace('QW', 'Q*W')
a = s.split('*')

print(max(map(len, a)))
