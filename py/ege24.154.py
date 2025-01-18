from itertools import product

f = open('ege24.154.txt')
s = f.readline().strip()

Found = False
k = 1

while not Found:
    for p in product('ABCEF', repeat = k):

        sp = ''.join(p)
        DspD = 'D' + sp + 'D'
        if DspD in s:
            print(len(DspD) - 2)
            Found = True
            break
    k += 1
