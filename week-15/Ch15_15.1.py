import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance_between_points(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return math.sqrt(dx**2 + dy**2)

point1 = Point(1, 2)
point2 = Point(4, 6)
print(distance_between_points(point1, point2))
