def dec2word(x, alpha):
    n = len(alpha)
    w = ''
    while x > 0:
        w = alpha[x % n] + w
        x //= n

    return w

alpha = 'AMPT'
i = 250 - 1
print(dec2word(i, alpha))
