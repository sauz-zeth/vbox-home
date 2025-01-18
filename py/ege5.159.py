for n in range(0, 256):
    ns = f"{bin(n)[2:]:>08s}"
    ns2 = ns.replace('0', 'x')
    ns2 = ns2.replace('1', '0')
    ns2 = ns2.replace('x', '1')

    if int(ns2, 2) - int(ns, 2) == 45:
        print(n)
