import math

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    print(f"Calling arc with r={r}, angle={angle}, arc_length={arc_length}, n={n}, step_length={step_length}, step_angle={step_angle}")
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def circle(t, r):
    print(f"Calling circle with r={r}")
    arc(t, r, 360)
