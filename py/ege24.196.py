f = open('ege24.196.txt')
s = f.read().strip()

s = s.replace('ZX', '#')
s = s.replace('ZY', '$')

w = ''
while w in s:
    w += '#'

l1 = len(w) - 1

w = ''
while w in s:
    w += '$'

l2 = len(w) - 1

print(max(l1, l2))

