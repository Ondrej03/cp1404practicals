"""
CP1404/CP5632 Practical - Guitar exercise
"""

class Guitar:

    current_year = 2024

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : €{self.cost}"

    def get_age(self):
        return self.current_year - self.year

    def is_vintage(self):
        return True if self.get_age() > 50 else False
