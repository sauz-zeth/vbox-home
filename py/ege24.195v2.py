f = open('24-191.txt')
s = f.readline().strip()

s = s.replace('A', '*A').replace('B', 'B*')

a = s.split('*')

n = 0
for w in a:
    if w.count('F') == 2 and len(w) >= 20:
        if w[0] == 'A' and w[-1] == 'B':
            if w.count('A') == 1 and w.count('B') == 1:
                n += 1

print(n)
