from itertools import permutations
import re

alpha = 'хочу в вуз'

print(sum(1 for s in map(''.join, set(permutations(alpha))) if re.fullmatch('[^у]\w* [^у]\w* [^у]\w*', s)) - 1)
