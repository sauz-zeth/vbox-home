for i in range(500, 0, -1):

    si = bin(i)[2:]
    si2 = list(reversed(si))
    si3 = []

    skip = 1
    for x in si2:
        if x == '1': skip = 0
        if not skip:
            si3.append(x)

    si3 = ''.join(si3)

    si3 = int(si3, 2)

    if si3 == 11:
        print(i)
        break
