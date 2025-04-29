def draw_rectangle(canvas, rect):
    x = rect.corner.x
    y = rect.corner.y
    bbox = [[x, y], [x + rect.width, y + rect.height]]
    canvas.rectangle(bbox, outline='black', fill=rect.color)

class Rectangle:
    def __init__(self, width, height, corner, color='green4'):
        self.width = width
        self.height = height
        self.corner = corner  
        self.color = color

def draw_point(canvas, point, color='black'):
    radius = 3 
    canvas.circle([point.x, point.y], radius, outline=None, fill=color)

class Circle:
    def __init__(self, center, radius, color='red'):
        self.center = center 
        self.radius = radius
        self.color = color

def draw_circle(canvas, circle):
    canvas.circle([circle.center.x, circle.center.y], circle.radius, outline=None, fill=circle.color)

def draw_czech_flag(canvas):
    
    canvas.rectangle([[-150, 0], [150, 100]], fill='white', outline='black')

    canvas.rectangle([[-150, -100], [150, 0]], fill='red', outline='black')

    points = [[-150, 100], [-150, -100], [0, 0]]
    canvas.polygon(points, fill='blue')

from swampy.World import World

world = World()
canvas = world.ca(width=500, height=500, background='white')
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

corner = Point(-50, -25)
rect = Rectangle(100, 50, corner, color='green4')
draw_rectangle(canvas, rect)

pt = Point(0, 0)
draw_point(canvas, pt)

circle = Circle(Point(75, 75), 30, 'blue')
draw_circle(canvas, circle)

draw_czech_flag(canvas)

world.mainloop()
