s = '>' + 20 * '1' + 40 * '3' + 15 * '2' + '<'

while '><' not in s:
    print(s)
    s = s.replace('>1', '3>', 1)
    s = s.replace('>2', '2>', 1)
    s = s.replace('>3', '1>', 1)

    s = s.replace('3<', '<1', 1)
    s = s.replace('2<', '<3', 1)
    s = s.replace('1<', '<2', 1)

s = s.replace('><', '0')
ssum = sum(map(int, list(s)))

print(ssum)
