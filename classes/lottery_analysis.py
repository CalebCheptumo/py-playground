from random import sample

class Lottery:
    """A class that represents a lottery"""

    def __init__(self, items):
        """Initialize the lottery attributes"""
        self.items = items

    def draw_lottery(self):
        """Draw 4 random items from the lottery"""
        return sample(self.items, 4)

# Create a lottery
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
lottery = Lottery(items)

# Create my ticket
my_ticket = ['1', '2', 'A', 'B']  # I'm using strings to match the items drawn

# Keep drawing until my ticket wins
attempts = 0
while True:
    attempts += 1
    winning_items = [str(item) for item in lottery.draw_lottery()]  # Convert winning items to strings
    if sorted(winning_items) == sorted(my_ticket):
        break

print(f"It took {attempts} attempts to win the lottery.")