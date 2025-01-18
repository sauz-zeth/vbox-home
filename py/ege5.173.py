for i in range(100, 0, -1):
    si = f"{i:08b}"
    si = si[:-1]
    si = si[::-1]
    i2 = int(si, 2)
    if i == i2:
        print(i)
        break
