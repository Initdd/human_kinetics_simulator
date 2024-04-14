import threading
import time
import pygame
from pygame.locals import *
import typing as tp
from src.Leg import Leg

# Initialize Pygame
pygame.init()
# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
pygame.display.set_caption("Human kinetics simulator")
clock = pygame.time.Clock()

# Constants
FPS = 60
INCREMENT = 5
INITIAL_ANGLES = (0, 0, 0)
INITIAL_POSITION = (100, 100)
LENGTH = 50

# Create a Leg object
actions = [
	(Leg.Part.DOWN, -45),
	(Leg.Part.MID, 45),
	(Leg.Part.DOWN, 45),
	(Leg.Part.UP, 45),
]
leg = Leg(LENGTH, INITIAL_POSITION, INITIAL_ANGLES, actions, INCREMENT)

# Add actions from the command line
def dispach_command() -> None:
	"""
		Dispatch a command from the command line

		Commands:
			- "help": Show the help message
			- "exit": Exit the program
			- action: Add a specified action to the leg

		Actions: Composed by: "part angle"
			e.g.: "UP 45" -> Move the UP part 45 degrees
		
		Parts:
			- UP
			- MID
			- DOWN

		Angles:
			- Any integer number
	"""
	command = input(">: ")
	if command == "help":
		print(dispach_command.__doc__)
	elif command == "exit":
		pygame.quit()
		quit()
	else:
		part, angle = command.split()
		if part not in ["UP", "MID", "DOWN"] or not angle.isdigit():
			print("Invalid command")
			return
		angle = int(angle)
		part = Leg.Part.from_str(part)
		actions.append((part, angle))

# set and start the command line thread
def command_loop() -> None:
	while True:
		dispach_command()

command_thread = threading.Thread(target=command_loop)
command_thread.start()

# Game loop
running = True
while running:
	# Set the frame rate
	clock.tick(FPS)

	# Handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Update game logic
	leg.dispach_actions()
	#print(leg.get_angles())

	# Render graphics
	screen.fill((0, 0, 0))  # Fill the screen with black

	# Add your drawing code here
	positions: tp.List[tuple[float, float]] = leg.get_crit_pos()
	pygame.draw.lines(screen, (255, 255, 255), False, positions, 5)
	for pos in positions:
		pygame.draw.circle(screen, (255, 0, 0), (int(pos[0]), int(pos[1])), 5)

	# Wait for a short while
	time.sleep(0.1)

	pygame.display.flip()  # Update the display
# Stop the command line thread
command_thread.join()
# Quit Pygame
pygame.quit()