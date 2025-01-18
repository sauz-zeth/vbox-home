from itertools import islice

def tuplewise(a, l = 2):
    return zip(*(islice(a, i, None) for i in range(l)))

f = open('24-181.txt')
s = f.readline().strip()

a = list(map(len, s.split('.')))

print(max(map(sum, tuplewise(a, 3))) + 2)
