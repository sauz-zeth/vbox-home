#1?1?1?1?1??1

n = int('101101', 2)

for i in range(2**6):
    i1, i2, i3, i4, i5, i6 = f"{i:06b}"

    x = f"1{i1}1{i2}1{i3}1{i4}1{i5}{i6}1"
    xd = int(x, 2)
    if xd % n == 0:
        print(xd, xd // n)
