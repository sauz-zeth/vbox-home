for x in range(14, -1, -1):
    l = int('13101', 15) + x * 15 + int('1303', 17) + x * 17
    if l % 11 == 0: break

print(l // 11)
