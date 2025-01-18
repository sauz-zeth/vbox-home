def word2dec(w, alpha):
    n = len(alpha)
    ch2d = dict(zip(alpha, range(n)))
    y = 0
    for ch in w:
        y = y * n + ch2d[ch]

    return y
        
alpha = "ДКМО"
n1 = word2dec('ДОМОК', alpha) 
n2 = word2dec('КОМОД', alpha) 

print(n2 - n1 + 1)

