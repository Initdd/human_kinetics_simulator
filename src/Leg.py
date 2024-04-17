
from enum import Enum
import typing as tp
from parts.limb import Limb
from parts.part import Part


# Constants
ANGLE_DEC_PLACES = 2
ANGLE_MAX = 360

def convert_to_positive_angle(angle: int) -> int:
	"""
		Function to convert an angle to a positive angle

		Args:
			angle: The angle to convert

		Returns:
			The positive angle
	"""
	return (angle + ANGLE_MAX) % ANGLE_MAX

class Leg(Limb):
	"""
		Class to represent a leg

		Attributes:
			length: The length of the leg
			position: The position of the leg
			actions: The actions to be executed
			increment: The increment to increase the angle of the leg
			action_idx: The action index for each part
			dispach_buffer: The dispach buffer
	"""

	def __init__(self, length: float, position: tp.Tuple[float, float], start_angles: tp.Tuple[int], actions: tp.List[tuple[Part, int]], increment: int) -> None:
		# Length of each part of the leg
		self.length = length
		# Position of the leg
		# Precisely, the position of the upper part of the leg
		self.position = position
		# Setup the leg with the angles and the respective positions
		self._setup(start_angles)
		# increment to increase the angle of the leg
		self.increment = increment
		# actions to be executed
		# These are absolute values
		# In other words, the angles are not relative to the current angle!
		# Format:
		# part_idx: angle
		self.actions = actions
		# actions list index for each leg part
		# It will be used to keep track of the current action of each part
		self.action_idx = [0 for _ in range(len(Part))]
		# dispach buffer. A triple buffer to keep track of the actions being executed
		# Format:
		# part_idx: angle
		self.dispach_buffer: tp.List[tp.Optional[int]] = self._set_dispach_buffer()

	def _set_dispach_buffer(self) -> tp.List[tp.Optional[int]]:
		"""
			Method to set the initial dispach buffer

			Returns:
				The dispach buffer
		"""
		initial_dispach_buffer = []
		# go through all the parts of the leg (these are the indexes of the dispach buffer)
		for i in range(len(Part)):
			# set the dispach_buffer[i] to the first action that has the index i
			for j, action in enumerate(self.actions):
				if action[0] == i:
					# because the we are iterating through the parts of the leg
	 				# we can just append the action to the dispach buffer
					initial_dispach_buffer.append(action[1])
					# increment the action index
					self.action_idx[i] += 1
					break
			else:
				# if there is no action for the part, append a None
				initial_dispach_buffer.append(None)
		return initial_dispach_buffer

	def inc_angle(self, part: int, angle: int) -> bool:
		"""
			Method to increase the angle of the leg

			Args:
				angle: The angle to increase
			
			Returns:
				Boolean indicating if the angle was increased
		"""

		# The increment will work like this:
		# 1. Check if it will be a positive or negative increment
		# 2. Set the increment to the distance between the old angle and the desired one
		# not past the maximum increment (self.increment)
		# 3. Increment the angle
		# 4. Check if the angle is the same as the desired angle
		# and return True if it is

		old_angle = self.get_angle(part)
		increment = self.increment

		# check if the increment needs to be negative
		pos_increment = (angle - old_angle) % ANGLE_MAX
		neg_increment = (old_angle - angle) % ANGLE_MAX
		increment = -increment if pos_increment > neg_increment else increment

		# get the distance between the old angle and the desired angle
		distance = abs(angle - old_angle)
		# check if the distance is less than the increment
		# if not, just add the increment to the angle
		if distance <= self.increment:
			# if the distance is less than the increment,
			# we will have to calculate the increment
			if distance != 0:
				if (increment > 0):
					increment = (distance % increment)
				elif (increment < 0):
					increment = -(distance % -increment)
				else:
					increment = 0
			else:
				# if the angle is the same as the desired angle, return True
				return True

		# increment the angle
		incremented_angle = old_angle + increment
		# set decimal values
		incremented_angle = round(incremented_angle, 2)

		# set the angle
		self.set_angle(part, incremented_angle)

		# check if the angle is the same as the desired angle
		return incremented_angle == angle
	
	def dispach_actions(self) -> None:
		"""
			Method to dispatch a list of parts to their respective angles
			It will go through the list, add new actions to the dispach list
			if the previous action was finished
		"""
		# Execute and clean the executed actions
		for part_idx, current_angle in enumerate(self.dispach_buffer):
			# execute the action
			# and then check if the action is done (is True)
			# if it is done, place a None
			if current_angle is not None:
				# execute the action
				done = self.inc_angle(part_idx, current_angle)
				# if the action is done, place a None
				if done:
					# set the action angle to None
					self.dispach_buffer[part_idx] = None

		# fill the dispach list with the new actions
		# Iterate through the actions beginning from the current action index
		for curr_action_idx in range(min(self.action_idx), len(self.actions)):
			# get the action
			action = self.actions[curr_action_idx]
			# extract the part index and the angle from the action
			part_idx, angle = action
			part_idx = part_idx.value
			# check if the action idx for the part
			# is less than the current action index
			# if it is, continue to the next action
			if curr_action_idx < self.action_idx[part_idx]: continue
			# before adding the action,
			# check if the current action is None
			# if it is, add the action to the dispach buffer
			if self.dispach_buffer[part_idx] is None:
				self.dispach_buffer[part_idx] = angle
				# increment the action index
				self.action_idx[part_idx] = curr_action_idx + 1
	
	
		
