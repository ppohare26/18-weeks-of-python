from vpython import *

scene.range = 256
scene.center = vector(128, 128, 128)

color_rgb = vector(0.1, 0.1, 0.9)  # blue

t = range(0, 256, 51)
for x in t:
    for y in t:
        for z in t:
            pos = vector(x, y, z)
            sphere(pos=pos, radius=10, color=color_rgb)

from vpython import *

scene.range = 256
scene.center = vector(128, 128, 128)

t = range(0, 256, 51)
for x in t:
    for y in t:
        for z in t:
            pos = vector(x, y, z)
            color_rgb = vector(x / 255, y / 255, z / 255)
            sphere(pos=pos, radius=10, color=color_rgb)

('CornflowerBlue', (0.392, 0.584, 0.929))

from vpython import *
from color_list import read_colors

scene.range = 1
scene.center = vector(0.5, 0.5, 0.5)

colors = read_colors()

for name, (r, g, b) in colors:
    pos = vector(r, g, b)
    sphere(pos=pos, radius=0.01, color=vector(r, g, b))
