a = [None] * (2024 + 1)
a[1] = 1
a[2] = 2

for n in range(3, 2024 + 1):
    a[n] = n * (n - 1) + a[n - 1] - a[n - 2]

print(a[2024] + a[2022] - a[2019])


    
