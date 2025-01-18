from itertools import permutations

n = 0
for s in map(''.join, permutations('АЙСБЕРГ', 7)):
    if s[0] != 'Й' and 'ЙА' not in s and 'ЙЕ' not in s:
        n += 1

print(n)
