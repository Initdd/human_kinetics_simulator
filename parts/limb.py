import typing as tp
from utils.line import Line
import math

class Limb:
	"""
		Class to represent a leg of the robot

		Attributes:
			name: The name of the leg
			length: The length of the leg
			angle: The angle of the leg
			position: The position of the leg
	"""

	def __init__(self, length: int, position: tp.Tuple[int, int], angles: tp.List[int]) -> None:
		# Length of each part of the leg
		self.length: int = length
		# Position of the leg
		# Precisely, the position of the upper part of the leg
		self.position: tp.Tuple[int, int] = position
		# Parts of the leg
		self.parts: tp.List[Line] = []
		# Setup the leg with the angles and the respective positions
		self._setup(angles)

	def _setup(self, angles: tp.List[int]) -> None:
		"""
			Method to setup the angles of the leg

			Args:
				angles: The angles of the leg
		"""
		self.parts = [Line() for _ in range(len(angles))]
		# Iterate over each part of the leg
		for i, angle in enumerate(angles):
			# Set the start point for the current part
			if i == 0: start_point = self.position
			else: start_point = self.parts[i - 1].end_point
			
			# Set the end point based on the length and angle
			end_point = (start_point[0] + self.length, start_point[1])
			
			# Set the position and angle for the current part
			self.parts[i].start_point = start_point
			self.parts[i].end_point = end_point
			self.parts[i].rotate_on_point(angle, start_point)
		
	def move(self, position: tp.Tuple[int, int]) -> None:
		"""
			Method to move the leg to a new position

			Args:
				position: The new position of the leg
		"""
		# Calculate the difference between the new position and the current position
		diff = (position[0] - self.position[0], position[1] - self.position[1])
		# Move the leg
		self.position = position
		for part in self.parts:
			part.start_point = (part.start_point[0] + diff[0], part.start_point[1] + diff[1])
			part.end_point = (part.end_point[0] + diff[0], part.end_point[1] + diff[1])

	def rotate_part(self, part: int, angle: int) -> None:
		"""
			Method to rotate a part of the leg

			The other parts of the leg will be updated

			Args:
				part: The part of the leg to rotate
				angle: The angle to rotate the part
		"""
		# Iterate over each part of the leg
		for i in range(part, len(self.parts)):
			# Rotate the part with the angle and the
			self.parts[i].rotate_on_point(angle, self.parts[part].start_point)

	def get_crit_pos(self) -> tp.List[int]:
		"""
			Method to get the positions of the leg

			Returns:
				The positions of the leg
		"""
		# Return the start point of each part and the end point of the last part (-1)
		return [part.start_point for part in self.parts] + [self.parts[-1].end_point]
	
	def set_angle(self, part: int, angle: int) -> None:
		"""
			Method to set the angle of a part of the leg

			Args:
				part: The part of the leg to set the angle
				angle: The angle to set
		"""
		# Get the current angle of the part
		current_angle = self.get_angle(part)
		# Rotate the part with the difference between the current angle and the angle
		self.rotate_part(part, angle - current_angle)

	def get_angle(self, part: int) -> int:
		"""
			Method to get the angle of a part of the leg

			Args:
				part: The part of the leg to get the angle

			Returns:
				The angle of the part
		"""
		# Get the angle of the part
		return self.parts[part].get_rotation()

	def get_angles(self) -> tp.List[int]:
		"""
			Method to get the angles of the leg

			Returns:
				The angles of the leg
		"""
		ret_angles = []
		# Iterate over each part of the leg
		for part in range(len(self.parts)):
			# Get the angle of the part and append it to the list
			ret_angles.append(self.get_angle(part))
		return ret_angles
	
	def get_length(self) -> int:
		"""
			Method to get the length of the leg

			Returns:
				The length of the leg
		"""
		# Just return the length of the leg
		# Because the length of each part is the same
		# ? Might give support for different lengths for each part
		return self.length
	
if __name__ == '__main__':
	# Test the Limb class
	limb = Limb(10, (0, 0), [45, 90])
