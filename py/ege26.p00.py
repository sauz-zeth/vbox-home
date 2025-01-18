f = open('ege26.p00.txt')
s, n = map(int, f.readline().split())
a = sorted(int(f.readline()) for i in range(n))
#a = sorted(int(x) for x in f if x != '\n')

for i in range(n):
    s -= a[i]
    if s < 0:
        print(i, end = ' ') 
        d = s + a[i]
        i1 = i - 1
        for j in range(i, n):
            if a[i1] + d < a[j]:
                print(a[j - 1])
                break
        break
        
