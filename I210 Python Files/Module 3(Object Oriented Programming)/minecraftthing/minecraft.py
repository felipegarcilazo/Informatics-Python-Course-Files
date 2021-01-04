import random

## Part One: Create mine

def create_mine(materials):
	mine = []

	# The depth of the mine should be between 10 and 100 elements.
	depth = random.randrange(10, 101)

	# Create a list of materials to represent the mine.
	# This is what we'll "dig through" in our main program.
	for i in range(depth):
		mine.append(random.choice(materials))
	
	print("Mine created.")

	return mine
