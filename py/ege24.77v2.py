f = open('ege24.77.txt')
s = f.read().strip()

alpha = set(s)
assert '.' not in alpha

for c in alpha:
    for i in range(len(s), 1, -1):
        s = s.replace(c * i, '.')

l = list(s)
l[0] = '.'
l[-1] = '.'
s = ''.join(l)

for c in alpha:
    s = s.replace(c, '?')

w = ''
while w in s:
    w += '?'

print(len(w) + 1)
