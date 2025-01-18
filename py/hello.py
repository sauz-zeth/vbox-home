#комментарий
print("Hello!", "How are you?"); print("Bye!")
print("Result: %o." % (10 + 5))
print("Hex->Dec:", 0x10)
print("Oct->Dec:", 0o10)
print("Bin->Dec:", 0b10)
#                  ^
#           двоичный литерал
print("Hex->Oct: %o" % 0x10)  
print("Hex->Oct:", oct(0x10))
print("Hex->Bin:", bin(0x10))

a = 0x10    #переменная
print(a)
a = 0b10
print(a)
print(type(a))
a = "aaaaaaa"
print(a, type(a))

for i in range(5):
    print(i)

print()

for i in range(-4, 5, 2):
    print(i)
    print("|")

print()

N = 100
s = 0
for i in range(1, N + 1):
    s += i
#    s = s + i
print(s)

print()

print(5 / 3)
print(5 // 3)
print(-5 // 3)
print(5 % 3)
print(-5 % 3)

print(bin(87626798))
