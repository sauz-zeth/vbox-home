from collections import Counter

def counter(a):
    return Counter(a).items()

a = [3, 1, 4, 3, 3, 2, 3, 4]
print(list(counter(a)))
