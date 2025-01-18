import re

fs = open('ege24.143.txt').read()

alpha = set(fs)

fs = fs.replace('Z', 'z')
fs = fs.replace('R', 'r')
fs = fs.replace('O', 'o')
fs = fs.replace('\n', '*')

for x in alpha:
    fs = fs.replace(x, '_')

a = fs.split('*')
print(sum(1 for s in a if re.search('z[zro_]ro', s)))
