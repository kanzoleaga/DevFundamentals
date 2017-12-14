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