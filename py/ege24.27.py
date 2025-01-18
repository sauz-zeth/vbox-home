f = open("ege24.27.txt")
s = f.read().strip()
s = s.replace('EAB', '?')
s = s.replace('?E', '#')
s = s.replace('#A', '*')

w1 = '*'
while w1 in s:
    w1 = '?' + w1

w1 = w1[1:]

a = (len(w1) - 1) * 3 + 5


w2 = '#'
while w2 in s:
    w2 = '?' + w2

w2 = w2[1:]

b = (len(w2) - 1) * 3 + 4


w3 = '' 
while w3 in s:
    w3 += '?'

w3 = w3[1:]

c = len(w3) * 3

print(max(a, b, c))
