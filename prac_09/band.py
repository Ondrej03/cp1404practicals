"""Band clas for CP1404"""

class Band:
    """Band class"""

    def __init__(self, name):
        """Construct a Band with a nam and empty musicians collection"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band"""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to band's collection"""
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            print(musician.play())