I = 5 * 1024 * 1024 * 8 #bit
v = 2**18 #bit/sec
Ia = I * 0.2
tzip = 7 # sec
tunzip = 1 # sec

tA = tzip + Ia / v + tunzip
tB = I / v

print(tA, tB)
print('A', tB - tA) 
