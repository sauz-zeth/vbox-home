f = open('ege24.154.txt')
s = f.readline().strip()

print(min(len(x) for x in s.split('D')[1:-1] if x != '') + 2)
