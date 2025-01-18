import ipaddress as ip

na = ip.ip_network('202.75.38.176/255.255.255.240')
print(f'{na[0]:_b}')

k = 0
for x in na:
    s = f"{x:b}"
    if '111' in s or '000' in s: continue

    k += 1

print(k)
