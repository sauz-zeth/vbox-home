a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = 0

if a > b:
    e = a
    a = b
    b = e
if b > c:
    e = b
    b = c
    c = e
if c > d:
    e = c
    c = d
    d = e

if a > b:
    e = a
    a = b
    b = e
if b > c:
    e = b
    b = c
    c = e

if a > b:
    e = a
    a = b
    b = e

print(a, b, c, d)
    

