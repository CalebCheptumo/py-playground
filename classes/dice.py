from random import randint

class Dice:
    """A class that represents a dice"""

    def __init__(self, sides=6):
        """Initialize the dice attributes"""
        self.sides = sides

    def roll_dice(self):
        """Simulate rolling the dice"""
        print(f"The dice rolled a {randint(1, self.sides)}")

# Create a 6-sided dice and roll it 10 times
dice = Dice()
for i in range(10):
    dice.roll_dice()

# Create a 10-sided dice and roll it 10 times
dice = Dice(10)
for i in range(10):
    dice.roll_dice()

# Create a 20-sided dice and roll it 10 times
dice = Dice(20)
for i in range(10):
    dice.roll_dice()

