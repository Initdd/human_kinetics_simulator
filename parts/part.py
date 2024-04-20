import typing as tp
from enum import Enum

class Part(Enum):
		"""
			Enum to represent the parts of the Limb
		"""
		UP = 0
		MID = 1
		DOWN = 2

		def get_others(self) -> tp.List[int]:
			"""
				Method to get the other parts of the Limb

				Returns:
					The other parts of the Limb
			"""
			# iterate through the parts of the Limb
			return [part for part in Part if part != self]

		def get_bottoms(self) -> tp.List[int]:
			"""
				Method to get the bottom parts of the Limb from a part

				Returns:
					The bottom parts of the Limb from the part
			"""
			return [part for part in Part if part > self]

		def __str__(self):
			"""
				Method to convert the part to a string

				Returns:
					The part as a string
			"""
			return self.name
		
		def __repr__(self):
			return self.__str__()
		
		def __eq__(self, other):
			return self.value == other
		
		def __ne__(self, other):
			return not self.__eq__(other)
		
		def __lt__(self, other):
			return self.value < other.value

		@classmethod
		def _validate_str_part(self, part: str) -> bool:
			"""
				Validate if a string is a valid part

				Valid parts: (UP, U), (MID, M), (DOWN, D)
			"""
			return part.upper() in ["UP", "MID", "DOWN"] or part.upper() in ["U", "M", "D"]
		
		# function to get the part from a string
		@classmethod
		def from_str(self, str_part: str) -> tp.Optional[int]:
			"""
				Method to get the part from a string

				Args:
					part: The part as a string

				Returns:
					The part as an integer or None if the part is invalid
			"""
			if not self._validate_str_part(str_part): return None
			return self.UP if str_part.upper() in ["UP", "U"] else self.MID if str_part.upper() in ["MID", "M"] else self.DOWN
	

if __name__ == "__main__":
	print(str(Part.UP))
	print(Part.UP.get_others())
	print(Part.UP.get_bottoms())
	print(Part.UP.from_str("up"))
	print(Part.UP.from_str("u"))
	print(Part.UP.from_str("mid"))
	print(Part.UP.from_str("m"))
	print(Part.UP.from_str("down"))
	print(Part.UP.from_str("d"))