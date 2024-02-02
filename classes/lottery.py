from random import sample

class Lottery:
    """A class that represents a lottery"""

    def __init__(self, items):
        """Initialize the lottery attributes"""
        self.items = items

    def draw_lottery(self):
        """Draw 4 random items from the lottery"""
        winning_items = sample(self.items, 4)
        print(f"Any ticket matching these 4 items wins a prize: {winning_items}")

# Create a lottery and draw 4 items
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
lottery = Lottery(items)
lottery.draw_lottery()