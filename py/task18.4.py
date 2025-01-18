n = int(input())
b = n
s = 0
while n > 0:
    s = s * 10 + n % 10
    n //= 10
print(s)
print(b + s)
