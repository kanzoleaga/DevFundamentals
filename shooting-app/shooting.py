import math

class Position(object):

	def __init__(self, x=0, y=0):
		self._x = x
		self._y = y

	def x(self):
		return self._x

	def y(self):
		return self._y

	def distance_to(self, other):
		delta_x = self.x() - other.x()
		delta_y = self.y() - other.y()
		return math.sqrt(delta_x ** 2 + delta_y ** 2)

	def __eq__(self, other):
		if (isinstance(other, Position)):
			return self.x() == other.x() and self.y() == other.y()
		else:
			return False

	def __str__(self):
		return "(" + str(self._x) + ", " + str(self._y) + ")"	

class Velocity(object):

	def __init__(self, start, end):
		self.start = start
		self.end = end

	def magnitude(self):
		return self.end.distance_to(self.start)

	def angle(self):
		# angle = tan-1(y/x)
		delta_y = self.end.y() - self.start.y()
		delta_x = self.end.x() - self.start.x()
		return math.degrees(math.atan2(delta_y, delta_x))


class Projectile(object):
	
	def __init__(self, position):
		self._position = position;

	def shoot(self, velocity):
		pass

	def position(self):
		return Position(5, 0)


