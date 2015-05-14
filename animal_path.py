__author__ = 'Frankie'

import math
class Point:

	def __init__(self, x, y, t):
		self.x = x # x coordinate of point
		self.y = y # y coordinate of point
		self.time = t # time when animal reaches this point

	def __eq__ (self, other):
		"""	If the coordinates of this point match the coordinates of the other point,
			the points are equal """

		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False

class Line:

	def __init__(self, A, B):

		self.start = A # Starting point of line segment
		self.end = B # Ending point of line segment
		self.length = math.sqrt(math.pow((self.start.x-self.end.x),2)+math.pow((self.start.y-self.end.y),2))

		# Length of the line segment

class Path:

	def __init__(self):

		self.line_segments = [] # List of line segments which make up the path
		self.length = 0 # Length of path
		self.straight_line = 0 # Length of straight line from start to end of path


	def add_to_path(self, line):
		"""	Adds a line segment to the end of the path"""
		self.line_segments.append(line)
		self.length += line.length
		self.calc_straight_line()


	def calc_straight_line(self):
		"""	Calculates the distance from the starting point to the ending point,
			and sets value to self.straight_line"""

		temp_line = Line(self.line_segments[0].start, self.line_segments[-1].end)
		self.straight_line = temp_line.length

	def calc_curviness(self):
		"""Returns the curviness of the path"""
		return self.straight_line/self.length

	def move_check(self):
		"""Checks to see if the animal has moved by comparing the starting point
			of the path to the ending point. Returns boolean"""

		if self.line_segments[0].start == self.line_segments[-1].end:
			return False
		else:
			return True

	def same_point_check(self):
		"""	Checks to see if the path consists of a line which has the same starting
			and ending point. Returns boolean"""

		if len(self.line_segments)==1 and self.line_segments[0].start == self.line_segments[0].end:
			return True
		else:
			return False