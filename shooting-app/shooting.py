import math

def cuadratic_equation (a, b, c):
	x = []
	d = b ** 2 - 4 * a * c  # discriminant
	print ("d: ",d)
	if d < 0:
		return [] #"This equation has no real solution"
	elif d == 0:
		x = [-b / 2 * a]
		return x #	"This equation has one solutions: ", x
	else: #"This equation has two solutions: ", x1, " and", x2
		x1 = (-b - math.sqrt(d)) / (2 * a)
		x2 = (-b + math.sqrt(d)) / (2 * a)
		x = [x1, x2]  # returns first the positive solution for a positive time
		return (x)


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
			return (self.x() == other.x() and self.y() == other.y())
		else:
			return False

	def __str__(self):
		return "(" + str(self._x) + ", " + str(self._y) + ")"	

class Velocity(object):

	def __init__(self, start, end):
		self.start = start
		self.end = end

	def delta_x (self):
		return self.end.x() - self.start.x()

	def delta_y (self):
		return self.end.y() - self.start.y()

	def magnitude(self):
		return self.end.distance_to(self.start)

	def angle(self):
		# angle = tan-1(y/x)
		return math.degrees(math.atan2(self.delta_y(), self.delta_x()))


class Projectile(object):
	
	def __init__(self, position):
		self._position = position;
		self.time = None
	def position (self):
		return (self.positon)


	def shoot(self, velocity):
		# Changes the inital postion to a new postion
		angle = velocity.angle()
		# The final position will be 0 for y then
		a = -1/2*9.8 # from  -1/2*g*t**2
		print ("a:", a)
		b = velocity.delta_y()
		print("b:", b)
		c = velocity.start.y()
		print("c:", c)
		t = cuadratic_equation(a, b, c)
		print (t)
		if t[0] >= 0:
			self.time = t[0]
		else:
			self.time = t[1]

		# Calculating the final position
		x = velocity.start.x() + velocity.delta_x()*self.time
		position = Position(x,0)
		self.position = position







