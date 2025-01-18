import ipaddress as ip

xa = ip.ip_address('220.128.112.142')
n = '220.128.96.0'

for p in range(32 + 1):
    na = ip.ip_network(f"{n}/{p}", 0)
    z = xa in na and n == str(na.network_address) 

    if z:
        print(na.netmask)
