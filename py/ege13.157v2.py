import ipaddress as ip

na = ip.ip_network('192.168.248.176/255.255.255.240')

k = 0
for x in na:
    s = f"{x:b}"
    if s.count('1') == s.count('0'):
        k += 1

print(k)
