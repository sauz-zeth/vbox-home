import re

f = open('24-212.txt')
s = f.readline().strip()

s = re.sub(r'[BCD]', 's', s)
s = re.sub(r'[AO]', 'g', s)
s = s.replace('sg', '.')

print(max(map(len, (m[0] for m in re.finditer(r'\.+', s)))))
