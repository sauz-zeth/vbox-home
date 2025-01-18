fs = open('ege24.143.txt').read()

alpha = set(fs)

fs = fs.replace('Z', 'z')
fs = fs.replace('R', 'r')
fs = fs.replace('O', 'o')
fs = fs.replace('\n', '*')

for x in alpha:
    fs = fs.replace(x, '_')

a = fs.split('*')
print(sum(1 for s in a if 'z_ro' in s or 'zzro' in s or 'zrro' in s or 'zoro' in s))
