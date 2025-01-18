from itertools import permutations
import re


alpha = 'хочу в вуз'

n = 0

for p in permutations(alpha):
    s = ''.join(p)
    
    if re.fullmatch('[^у]\w* [^у]\w* [^у]\w*', s):
        n += 1


print(n - 1)
