import math
from utils.point import rotate_point

class Line:
	"""
	Represents a line in a two-dimensional space.

	Attributes:
		start_point: The coordinates of the start point of the line.
		end_point: The coordinates of the end point of the line.
	"""

	def __init__(self, start_point: tuple[float, float] = (0, 0), end_point: tuple[float, float] = (0, 0)):
		self.start_point = start_point
		self.end_point = end_point

	def length(self) -> float:
		"""
		Calculates and returns the length of the line.

		Returns:
			float: The length of the line.
		"""
		return ((self.end_point[0] - self.start_point[0])**2 + (self.end_point[1] - self.start_point[1])**2)**0.5

	def slope(self) -> float:
		"""
		Calculates and returns the slope of the line.

		Returns:
			float: The slope of the line. If the line is vertical (denominator is zero), returns None.
		"""
		if self.end_point[0] == self.start_point[0]:
			# Line is vertical, slope is undefined
			return None
		else:
			return (self.end_point[1] - self.start_point[1]) / (self.end_point[0] - self.start_point[0])


	def is_parallel(self, other_line: 'Line') -> bool:
		"""
		Checks if the line is parallel to another line.

		Args:
			other_line: The other line to compare with.

		Returns:
			bool: True if the lines are parallel, False otherwise.
		"""
		return self.slope() == other_line.slope()

	def is_perpendicular(self, other_line: 'Line') -> bool:
		"""
		Checks if the line is perpendicular to another line.

		Args:
			other_line: The other line to compare with.

		Returns:
			bool: True if the lines are perpendicular, False otherwise.
		"""
		if self.slope() is None and other_line.slope() == 0:
			# the line is vertical and the other line is horizontal
			return True
		elif self.slope() == 0 and other_line.slope() is None:
			# the line is horizontal and the other line is vertical
			return True
		elif self.slope() is not None and other_line.slope() is not None:
			# the lines are neither vertical nor horizontal
			return self.slope() * other_line.slope() == -1
		else:
			# the lines are either both vertical or both horizontal
			return False

	def translate(self, dx: float, dy: float) -> None:
		"""
		Translates the line by the given offsets.

		Args:
			dx: The offset in the x-direction.
			dy: The offset in the y-direction.
		"""
		self.start_point = (self.start_point[0] + dx, self.start_point[1] + dy)
		self.end_point = (self.end_point[0] + dx, self.end_point[1] + dy)

	def get_rotation(self) -> float:
		"""
		Returns the rotation of the line in degrees.

		Returns:
			float: The rotation of the line in degrees.
		"""
		
		# Calculate the angle using arctan2
		y = self.end_point[1] - self.start_point[1]
		x = self.end_point[0] - self.start_point[0]
		angle = math.degrees(math.atan2(y, x))
		
		# Ensure the angle is within the range of 0 to 360 degrees
		if angle < 0:
			angle += 360
		elif angle >= 360:
			angle -= 360
		
		return angle

	def rotate_on_origin(self, angle: float) -> None:
		"""
		Rotates the line around the origin by the given angle.
		The rotation is done clockwise.

		Args:
			angle: The angle of rotation in degrees.
		"""
		self.start_point = rotate_point(self.start_point, (0, 0), angle)
		self.end_point = rotate_point(self.end_point, (0, 0), angle)
		
	def rotate_on_point(self, angle: float, center: tuple[float, float]) -> None:
		"""
		Rotates the line around a given point by the given angle.
		The rotation is done clockwise.

		Args:
			angle: The angle of rotation in degrees.
			point: The coordinates of the rotation point.
		"""
		self.start_point = rotate_point(self.start_point, center, angle)
		self.end_point = rotate_point(self.end_point, center, angle)
	
	def __str__(self) -> str:
		"""
		Returns a string representation of the line.

		Returns:
			str: A string representation of the line.
		"""
		return f"Line({self.start_point}, {self.end_point})"
	