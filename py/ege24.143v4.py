fs = open('ege24.143.txt').read()
a = fs.split()

n = 0
for l in a:
    for i in range(3, len(l)):
        if l[i - 3] == 'Z' and l[i - 1] == 'R' and l[i] == 'O':
            n += 1
            break

print(n)
