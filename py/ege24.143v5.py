fs = open('ege24.143.txt').read()
a = fs.split()

print(sum(1 for l in a for i in range(3, len(l)) if l[i - 3] == 'Z' and l[i - 1] == 'R' and l[i] == 'O'))
