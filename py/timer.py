from time import perf_counter as pc

t0 = 0

def start():
    global t0
    t0 = pc()

def show():
    t1 = pc()
    dt = t1 - t0
    print('\x1b[33;1m%.3f ms\x1b[0m' % (dt * 1000))
