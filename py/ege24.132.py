f = open('24-j1.txt', encoding = 'cp1251')
s = f.readline().strip()

w0 = 'КОТ'

w = ''
while w in s:
    w += w0

print(len(w) // 3 - 1)
