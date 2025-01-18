from collections import deque
import sys
from time import perf_counter as pc

d = deque(range(5))
print(d)
d.append(15)
d.appendleft(23)
print(d)
print(d[1])
#print(d[1:3])

l = []

def listAppendLeft():

    for i in range(10**5):
        l.insert(0, i)

    print(sys.getsizeof(l))
    print(sys.getsizeof(l[0]))

#listAppendLeft()

def dequeAppendLeft():
    d.clear()

    for i in range(10**6):
        d.appendleft(i)

    print(sys.getsizeof(d))
    print(sys.getsizeof(d[0]))

dequeAppendLeft()

def dequeGet():
    for i in range(1000):
        x = d[5 * 10**5]

t0 = pc()

dequeGet()

t1 = pc()

print(round((t1 - t0), 3))

l = list(range(10**6))

def listGet():
    for i in range(1000):
        x = l[5 * 10**5]

t0 = pc()

listGet()
 
t1 = pc()

print(round((t1 - t0), 3))


w = deque([], 5)
print(w)

for i in range(10):
    w.append(i)
    print(w)

