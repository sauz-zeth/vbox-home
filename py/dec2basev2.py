i = int(input())
b = int(input())
k = 0
s = 0
while i > 0:
    s = s * b + i % b
    i //= b
    k += 1
    print(i, s, k)
for i in range(k):
    print(s % b, end = "")
    s //= b
print()
