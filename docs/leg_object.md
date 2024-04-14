# Leg Class

The `Leg` class represents a leg of the robot. It is a subclass of the `Limb` class and is defined in the `Leg.py` module.

## Constructor

The constructor of the `Leg` class has the following signature:

```python
def __init__(self, length: int, position: Tuple[int, int], start_angles: Tuple[int, int, int], actions: List[Tuple[Part, int]], increment: int):
```
- `length`: The length of the leg
- `position`: The position of the leg, namely the position of the upper part
- `start_angles`: The initial angles of the leg parts
- `actions`: The actions to be executed
- `increment`: The increment to increase the angle of the leg

## Attributes

- `length`(int): The length of the leg. For now, it is a fixed value
for every part of the leg
- `position`(Tuple(int)): The position of the leg, namely the position of the upper part
- `actions`(List(Tuple(Part, int))): The actions to be executed.   
Each action is a tuple with two elements:
	- The part of the leg to be rotated
	- The angle to rotate the part
- `increment`(int): The increment to increase the angle of the leg
- `action_idx`: The action index for each part. Used to keep track of the last action executed
- `dispach_buffer`(List(Tuple(Part, int))): The dispach buffer

## Enumerations

- `Part`: An enumeration to represent the parts of the leg. It has the following values:
	- `UP`: The upper part of the leg
	- `MID`: The middle part of the leg
	- `DOWN`: The lower part of the leg

## Methods

- `dispatch_actions(self)`: Execute the actions defined in the `actions` attribute

## Usage

```python
from Leg import Leg

# Set the actions to be executed
actions = [
	(Part.UP, 45),
	(Part.MID, 45),
	(Part.DOWN, 45)
]

# Create a new Leg instance
leg = Leg(
	length=10,
	position=(0, 0),
	start_angles=(0, 0, 0),
	actions=actions,
	increment=5
)

# Execute the actions
leg.dispatch_actions()

```