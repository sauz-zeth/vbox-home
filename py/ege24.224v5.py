import re

f = open('24-224.txt')
s = f.readline().strip()

# BACAB -> BAC CAB
# CABAC -> CAB BAC

# BACABACAB -> BAC CABACAB -> BAC CAB BACAB -> BAC CAB BAC CAB
# BACABACABACAB -> BAC CABACABAC CAB -> BAC CAB BACABAC CAB -> BAC CAB BAC CABAC CAB -> BAC CAB BAC CAB BAC CAB
# CABACABACABAC -> CABAC CABACABAC -> CAB BAC CAB BACABAC -> CAB BAC CAB BAC CABAC -> CAB BAC CAB BAC CAB BAC

for _ in range(2):
    s = s.replace('BACAB', 'BAC CAB').replace('CABAC', 'CAB BAC')

print(max(len(m[0]) for m in re.finditer(r'(BAC|CAB)+', s)))
