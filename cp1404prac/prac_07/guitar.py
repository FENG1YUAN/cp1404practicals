"""
CP1404/CP5632 Practical
Author: FENG YUAN
Time: 15 minutes
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar based on the current year."""
        current_year = 2022  # Adjust accordingly
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Less than operator for sorting Guitars by year."""
        return self.year < other.year