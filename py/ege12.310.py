sa0 = ['1'] * 204
lmax = 0
smax = ''

for i in range(203):
    sa = sa0[:]
    sa[i] = '2'
    s = ''.join(sa)

    while '111' in s or '222' in s:
        if '111' in s:
            s = s.replace('111', '22', 1)
        else:
            s = s.replace('222', '11', 1)

    l = len(s)
    if l > lmax:
        lmax = l
        smax = s

print(smax)
