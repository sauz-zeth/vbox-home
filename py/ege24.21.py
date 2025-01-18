f = open("ege24.21.txt")
s = f.read().strip()
s = s.replace('A', '?')
s = s.replace('B', '?')
s = s.replace('C', '?')

w = ''

while w in s:
    w += '?'

print(len(w) - 1)
