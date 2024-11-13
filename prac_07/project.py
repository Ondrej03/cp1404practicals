"""
CP1404/CP5632 Practical - Project Management Program
"""

class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """
        Compare projects primarily by completion status (incomplete projects come before complete),
        and then by priority.
        """
        if self.is_complete() != other.is_complete():
            return not self.is_complete()
        return self.priority < other.priority

    def __str__(self):
        """Return a string representation of the project with its details."""
        return (f"{self.name}, start: {self.start_date}, priority: {self.priority}, estimate: ${self.cost_estimate}, "
                f"completion: {self.completion_percentage}%")

    def is_complete(self):
        """Return True if the project is complete, determined by a completion percentage of 100%."""
        return self.completion_percentage == "100"
