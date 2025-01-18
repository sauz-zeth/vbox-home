f = open('ege26.59v2.txt')
a = list(f)

for i in range(len(a) - 1, -1, -1):
    a[i] = a[i].replace('\t', '')
    if '1001' in a[i]:
        print(i)
        print(a[i].index('1001'))
        break
        
