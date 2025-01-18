f = open("ege24.27.txt")
s = f.read().strip()
s = s.replace('EAB', '?')

w1 = 'EA'
while w1 in s:
    w1 = '?' + w1

w1 = w1[1:]

a = w1.count('?') * 3 + 2


w2 = 'E'
while w2 in s:
    w2 = '?' + w2

w2 = w2[1:]

b = w2.count('?') * 3 + 1

w3 = '' 
while w3 in s:
    w3 += '?'

w3 = w3[1:]

c = w3.count('?') * 3

print(max(a, b, c))
