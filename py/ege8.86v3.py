def word2dec(w, alpha):
    y = 0
    n = len(alpha)
    for ch in w:
        d = alpha.index(ch)
        y = y * n + d

    return y


alpha = 'ВЕКНО'

print(word2dec('ОНННЕ', alpha) + 1)
