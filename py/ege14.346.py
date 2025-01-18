for x in range(15):
    l = int('12305', 15) + x * 15 + int('10233', 15) + x * 15**3
    if l % 14 == 0: break

print(l // 14)
