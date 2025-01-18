from collections import Counter

f = open('24-235.txt')
s = f.readline().strip()

for c in set(s):
    s = s.replace(f'{c}{c}', f'{c}.{c}').replace(f'{c}{c}', f'{c}.{c}')

a = s.split('.')
m = max(len(x) for x in a)
ma = [x for x in a if len(x) == m]

print(max(Counter(ma[-1]).values()))
