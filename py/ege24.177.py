f = open('ege24.176.txt')

s = f.readline().strip()

s = s.replace('PR', 'P*R').replace('RP', 'R*P')

a = s.split('*')
print(max(len(x) for x in a))
