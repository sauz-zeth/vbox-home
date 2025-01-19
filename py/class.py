class Point():
    index_max = 0

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
        Point.index_max += 1
    
    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        s = '{'
        for k, v in self.__dict__.items():
            s += f"'{k}': {v}, "
        s = s[:-2] + '}'

        return s

    def __add__(self, v):
        print('add')
        p = Point()
        p.__dict__.update(self.__dict__)
        p += v
        return p

    def __radd__(self, v):
        print('radd')
        return self + v
        
    def __iadd__(self, v):
        if type(self) is type(v):
            for k in self.__dict__:
                if hasattr(v, k):
                    setattr(self, k, getattr(self, k) + getattr(v, k))
                else:
                    setattr(self, k, getattr(self, k))
            for k in vars(self):
        else:
                setattr(self, k, getattr(self, k) + v)

        return p


    @staticmethod
    def instanceCount():
        return Point.index_max

    def print(self):
        print(f"x: {self.x}, y: {self.y}, z: {self.z}")

    
p = Point()
p.x = 1
p.y = 2
p.z = 5
p.t = 3
print(p.x)
print(dir(p))
print(vars(p))
print(p.__dict__)
print("p:", p)

q = Point(1, 5)
print(vars(q))
print("__str__:", q)
q.print()
f = q.print
f()
print(q.print)
Point.print(q)
print(Point.print)

print(q.index_max)
print(Point.index_max)
print(vars(q))
print(vars(Point))
print(Point.instanceCount())
print(q.instanceCount())
print(q.instanceCount)

print(p)
print(q)
r = p + q
print(r)
v = r + 50
print(v)
v = 50 + r
print(v)
v += p
print(v)
v += 20
print(v)
