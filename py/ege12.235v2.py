from random import shuffle

l = list('1' * 10 + '2' * 20 + '3' * 30)
shuffle(l)
s = '>' + ''.join(l)
print(s)


while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '1>', 1)

print(sum(map(int, s[:-1])))
