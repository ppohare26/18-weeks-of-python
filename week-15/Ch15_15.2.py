class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


corner_point = Point(0, 0)
my_rectangle = Rectangle(100, 50, corner_point)

print(f"Before move: ({my_rectangle.corner.x}, {my_rectangle.corner.y})")
move_rectangle(my_rectangle, 10, 20)
print(f"After move: ({my_rectangle.corner.x}, {my_rectangle.corner.y})")
