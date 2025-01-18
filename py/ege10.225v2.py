import re

f = open('10-222.txt')
s = f.read()

count = lambda r: len(re.findall(r, s)) 
print(count(r'готов') - count(r'\bготов\b'))
