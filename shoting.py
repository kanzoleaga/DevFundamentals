import math

class Position (object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def x (self):
        return (self._x)
    def y (self):
        return (self._y)
    def distance_to(self, other):
        if self.x == other.x() and self.y == other.y(): return 0
        delta_x = self.x() - other.x()
        delta_y = self.y() - other.y()
        return math.sqrt(delta_x**2-delta_y**2)

class Velocity (self, start, end)
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def magnitude (self)
        # if self.start.x () == self.end.x () and self.start.y () == self.end.y ():
        #     return 0
        return (distance_to (self.start, self.end))





