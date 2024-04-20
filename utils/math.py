def is_number(s: str) -> bool:
	"""
		Check if a string is a number
	"""
	try:
		float(s)
		return True
	except ValueError:
		return False