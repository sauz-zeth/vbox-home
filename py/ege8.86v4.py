def word2dec(w, alpha):
    y = ''
    n = len(alpha)
    for ch in w:
        d = alpha.index(ch)
        y += str(d)

    return int(y, n)


alpha = 'ВЕКНО'

print(word2dec('ОНННЕ', alpha) + 1)
