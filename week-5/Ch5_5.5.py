import turtle

def koch_curve(t, length, n):
    if n == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, n - 1)
        t.left(60)
        koch_curve(t, length, n - 1)
        t.right(120)
        koch_curve(t, length, n - 1)
        t.left(60)
        koch_curve(t, length, n - 1)

def draw_koch_curve(order, size):
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)  
    
    t.penup()
    t.goto(-size // 2, 0)
    t.pendown()

    koch_curve(t, size, order)

    screen.mainloop()

draw_koch_curve(4, 300)
