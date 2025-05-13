class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)
p1 = Point(2, 3)
p2 = Point(4, 1)
p3 = p1.add(p2)

print(p3) 
