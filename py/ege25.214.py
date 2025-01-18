#1?1?1?1?1??1

n = int('101101', 2)

for i1 in range(2):
    for i2 in range(2):
        for i3 in range(2):
            for i4 in range(2):
                for i5 in range(2):
                    for i6 in range(2):
                        x = f"1{i1}1{i2}1{i3}1{i4}1{i5}{i6}1"
                        xd = int(x, 2)
                        if xd % n == 0:
                            print(xd, xd // n)
