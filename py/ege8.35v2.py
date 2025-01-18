def word2dec(w, alpha):
    n = len(alpha)
    y = 0
    for ch in w:
        d = alpha.index(ch)
        y = y * n + d

    return y
        
alpha = "ДКМО"
n1 = word2dec('ДОМОК', alpha) 
n2 = word2dec('КОМОД', alpha) 

print(n2 - n1 + 1)

