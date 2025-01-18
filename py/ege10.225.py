import re

f = open('10-222.txt')
s = f.read()

print(len(re.findall(r'\w*готов\w+|\w+готов\w*', s)))
