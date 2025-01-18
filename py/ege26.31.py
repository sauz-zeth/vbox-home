from math import ceil

f = open('ege26.31.txt')
N = int(f.readline())
a = [*map(int, f)][:N]

asmall = [x for x in a if x <= 100]
abig = sorted(x for x in a if x > 100)
adisc = abig[:len(abig) // 2]
s = sum(asmall) + sum(abig) - sum(adisc) + ceil(sum(adisc) * 0.9)

print(s, max(adisc))
