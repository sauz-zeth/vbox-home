a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = 0

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    c, d = d, c

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b

if a > b:
    a, b = b, a


print(a, b, c, d)
    

