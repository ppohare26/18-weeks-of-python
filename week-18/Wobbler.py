"""This module contains code from Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from swampy.TurtleWorld import *
import math
import random

class Wobbler(Turtle):
    def __init__(self, clumsiness=0.5, speed=1.0):
        Turtle.__init__(self)
        self.set_clumsiness(clumsiness)
        self.set_speed(speed)

    def set_clumsiness(self, c):
        self.clumsiness = c

    def set_speed(self, s):
        self.speed = s

    def step(self):
        self.steer()
        self.wobble()
        self.move()

    def steer(self):
        pass

    def wobble(self):
        angle = random.gauss(0, 1) * self.clumsiness
        self.rt(angle)

    def move(self):
        dist = random.random() * self.speed
        self.fd(dist)


def make_world(turtle_class):
    """Makes a TurtleWorld and populates it with Turtles.

    turtle_class: class object to instantiate
    """
    world = TurtleWorld()
    for i in range(3):
        turtle = turtle_class()
        turtle.set_color('blue')
        turtle.delay = 0.01

    return world


if __name__ == '__main__':
    make_world(Wobbler)
    wait_for_user()
