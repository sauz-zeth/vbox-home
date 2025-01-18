f = open("ege24.27.txt")
s = f.read().strip()
alpha = 'EAB'


w = ''
for i in range(len(s)):
    x = alpha[i % 3]
    w += x
    if w not in s:
        print(len(w) - 1)
        break
        

