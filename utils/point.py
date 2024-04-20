import math
from typing import Tuple

DEC_VAL = 5
ANGLE_MAX = 360


def rotate_point(point: Tuple[float, float], center: Tuple[float, float], angle: float) -> Tuple[float, float]:
	angle_rad = math.radians(angle)
	x: float = point[0] - center[0]
	y: float = point[1] - center[1]
	new_x: float = round(x * math.cos(angle_rad) - y * math.sin(angle_rad), DEC_VAL)
	new_y: float = round(x * math.sin(angle_rad) + y * math.cos(angle_rad), DEC_VAL)
	return (new_x + center[0], new_y + center[1])

def convert_to_positive_angle(angle: int) -> int:
	"""
		Function to convert an angle to a positive angle

		Args:
			angle: The angle to convert

		Returns:
			The positive angle
	"""
	return (angle + ANGLE_MAX) % ANGLE_MAX