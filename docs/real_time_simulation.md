# Human Kinetics Simulator Command-Line Interface
## Overview
The Human Kinetics Simulator provides a command-line interface (CLI) for controlling the actions and movements of a simulated human leg. This CLI allows users to interactively input commands to manipulate the leg's movements in real-time.

## Usage
To use the command-line interface, run the Python script and enter commands through the command-line interface. The following sections outline the available commands and their syntax.

### Commands
#### help
Displays the help message, providing information on available commands and their usage.

##### Syntax:

```bash
help
```
#### exit
Exits the program, terminating the simulation and closing the application window.

##### Syntax:

```bash
exit
```

### Action Commands
Action commands are used to add specified actions to the leg, controlling its movement. Each action consists of a part and an angle.

#### Syntax:

```
{part} {angle}
```

- `{part}`: Specifies the part of the leg to move. Valid values are:  
	- UP: Upper part of the leg.
	- MID: Middle part of the leg.
	- DOWN: Lower part of the leg.
- `{angle}`: Specifies the angle by which to move the specified leg part. Must be an integer value.

#### Examples:

```
UP 45
MID -30
DOWN 60
```
### Parts and Angles
#### Parts
The leg is divided into three parts, each representing a segment of the leg's anatomy. These parts correspond to the thigh, knee, and shin, respectively:

- UP: Upper part (thigh) of the leg.
- MID: Middle part (knee) of the leg.
- DOWN: Lower part (shin) of the leg.

#### Angles
Angles represent the degree of rotation applied to each leg part. Positive angles indicate clockwise rotation, while negative angles indicate counterclockwise rotation. Angles must be specified as integer values.

### Example Usage
Start the program.  
Enter commands to manipulate the leg's movements, using the specified syntax.  
View the updated leg positions in the application window.
Note  
Invalid commands will result in error messages being displayed in the command-line interface.  
Ensure the application window remains visible to observe the effects of entered commands on the leg's movements.  
