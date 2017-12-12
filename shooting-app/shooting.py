import math
from cuadratic import *

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
			if self.x() == other.x() and self.y() == other.y():
				return True
		return False

	def __str__(self):
		return "(" + str(self._x) + ", " + str(self._y) + ")"	

class Velocity(object):

	def __init__(self, start, end):
		self.start = start
		self.end = end

	def magnitude(self):
		return self.end.distance_to(self.start)

	def delta_x (self):
		return (self.end.x() - self.start.x())

	def delta_y (self):
		return (self.end.y() - self.start.y())

	def angle(self):
		# angle = tan-1(y/x)
		delta_y = self.end.y() - self.start.y()
		delta_x = self.end.x() - self.start.x()
		return math.degrees(math.atan2(delta_y, delta_x))


class Projectile(object):
	
	def __init__(self, position):
		self._position = position
		self._time = None

	def position(self):
		return (self._position)

	def shoot(self, velocity):
		# Changes the inital postion to a new postion
		#angle = velocity.angle()
		#if angle > 0 and angle < 90:
		a = -1/2*9.8 # from  -1/2*g*t**2
		#print("a: ", a)
		#print ("velocity.end.y() :", velocity.end.y())
		#print("velocity.start.y() :", velocity.start.y())
		b = velocity.end.y() - velocity.start.y()
		#print("b: ", b)
		c = velocity.start.y()
		#print("c: ", c)
		t = cuadratic_equation(a, b, c)
		#print("t: ", t)
		# Taking only the positive value from solutions to this equation, since the time is positive
		if t[0] >= 0:
			self._time = t[0]
		else:
			self._time = t[1]
		# Calculating the final position
		final_x = round (velocity.start.x() + (velocity.delta_x()*self._time), 2)
		self._position = Position(final_x,0)
		print(self.position())