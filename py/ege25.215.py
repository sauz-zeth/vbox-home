#2?1?2?1?2?1

for i1 in range(2, -1, -1):
    for i2 in range(2, -1, -1):
        for i3 in range(2, -1, -1):
            for i4 in range(2, -1, -1):
                for i5 in range(2, -1, -1):
                    x = f"2{i1}1{i2}2{i3}1{i4}2{i5}1"
                    xd = int(x, 3)
                    if xd % 148 == 0:
                         print(xd, xd // 148)
