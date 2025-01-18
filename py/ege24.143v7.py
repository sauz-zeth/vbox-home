import re

fs = open('ege24.143.txt').read()

print(sum(1 for l in fs.split() if re.search('Z.RO', l)))
