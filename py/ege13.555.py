from ipaddress import *

n = 0
for ip in ip_network('112.208.0.0/255.255.128.0'):
    i = int(ip)
    s = f"{i:032b}"
    if s.count('1') % 11 == 0:
        n += 1
print(n)
