f = open("file.txt")

while True:
    l = f.readline()
    if l == '': break
    if l == '\n': continue
    x = int(l)

    print(x)

print()
f.seek(0)

for l in f:
    if l == '\n': continue
    x = int(l)
    print(x)

print()
f.seek(0)

print(list(f))
f.seek(0)

#print(list(map(int, f)))
#f.seek(0)

print([int(l) for l in f if l != '\n'])
f.seek(0)

r = [print(int(l)) for l in f if l != '\n']
f.seek(0)
print(r)

print(*(int(l) for l in f if l != '\n'), sep = '\n')
f.seek(0)

