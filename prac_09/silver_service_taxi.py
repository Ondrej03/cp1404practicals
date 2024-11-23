"""
CP1404/CP5632 Practical
Silver service class
"""

from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Represents a Silver Service Taxi object"""

    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver service Taxi instance."""

        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def __str__(self):
        """Return the price for the taxi trip."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
