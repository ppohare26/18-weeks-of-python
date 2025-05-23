from Wobbler import *

class Tagger(Wobbler):
    pass

make_world(Tagger)

import math

class Tagger(Wobbler):

    def steer(self):
        dx = -self.x
        dy = -self.y
        angle = math.atan2(dy, dx)
        angle = math.degrees(angle)
        self.heading = angle

def steer(self):
    margin = 100
    if abs(self.x) > margin or abs(self.y) > margin:
        dx = -self.x
        dy = -self.y
    else:
        dx = -self.x
        dy = -self.y

    angle = math.atan2(dy, dx)
    self.heading = math.degrees(angle)

def steer(self):
    nearest = None
    min_dist = float('inf')

    for other in self.world.animals:
        if other == self:
            continue
        dx = other.x - self.x
        dy = other.y - self.y
        dist = math.hypot(dx, dy)
        if dist < min_dist:
            min_dist = dist
            nearest = other

    if nearest:
        dx = nearest.x - self.x
        dy = nearest.y - self.y
        angle = math.degrees(math.atan2(dy, dx))
        self.heading = angle

class Tagger(Wobbler):

    def __init__(self):
        Wobbler.__init__(self)
        self.color = 'Black'

    def steer(self):
        # If I am "it", chase others
        if self.color == 'Red':
            nearest = self.find_nearest()
            if nearest and self.distance(nearest) < 10:
                nearest.color = 'Red'
                self.color = 'Black'
            else:
                self.face(nearest)
        else:
            # If not "it", run away from the one who is "it"
            chaser = self.find_chaser()
            if chaser:
                self.run_from(chaser)

    def find_nearest(self):
        nearest = None
        min_dist = float('inf')
        for other in self.world.animals:
            if other == self:
                continue
            d = self.distance(other)
            if d < min_dist:
                min_dist = d
                nearest = other
        return nearest

    def find_chaser(self):
        for other in self.world.animals:
            if other != self and other.color == 'Red':
                return other
        return None

    def run_from(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        angle = math.atan2(dy, dx)
        self.heading = math.degrees(angle)

    def face(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        angle = math.atan2(dy, dx)
        self.heading = math.degrees(angle)

from Wobbler import *

class Tagger(Wobbler):
    def steer(self):
        # Always steer toward the origin for now
        dx = -self.x
        dy = -self.y
        angle = math.atan2(dy, dx) * 180 / math.pi
        turn = angle - self.heading
        self.rt(turn)

world = make_world(Tagger)
world.animals[0].color = 'Red'  # First one is 'It'
wait_for_user()
