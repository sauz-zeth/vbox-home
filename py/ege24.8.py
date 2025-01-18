f = open("ege24.8.txt")
s = f.read().strip()

w = ''

while w in s:
    w += 'C'

print(len(w) - 1)
