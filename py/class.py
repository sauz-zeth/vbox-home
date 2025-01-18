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
