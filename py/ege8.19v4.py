def dec2word(x, alpha):
    n = len(alpha)
    l = []
    while x > 0:
        l.append(alpha[x % n])
        x //= n

    return ''.join(reversed(l))

alpha = 'AMPT'
i = 250 - 1
print(dec2word(i, alpha))
