from random import shuffle

ssummax = 0

while True:
    l = list(40 * '3' + 20 * '1' + 15 * '2')
    shuffle(l)
    s = '>' + ''.join(l) + '<'

    while '><' not in s:
        s = s.replace('>1', '3>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>3', '1>', 1)

        s = s.replace('3<', '<1', 1)
        s = s.replace('2<', '<3', 1)
        s = s.replace('1<', '<2', 1)

    s = s.replace('><', '0')
    ssum = sum(map(int, list(s)))

    if ssum > ssummax:
        ssummax = ssum
        print(ssum)
