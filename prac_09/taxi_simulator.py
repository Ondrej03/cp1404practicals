"""Taxi simulator program for CP1404"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def display_taxis(taxis):
    """Display a numbered list of available taxis."""
    print("Taxis available:")
    for index, taxi in enumerate(taxis):
        print(f"{index} - {str(taxi)}")


def main():
    """Run the main taxi simulator program."""
    current_taxi = None
    current_bill = 0

    print("Let's drive!")
    print(MENU)

    while (user_input := input(">>> ").lower()) != "q":
        if user_input == "c":
            display_taxis(TAXIS)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = TAXIS[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid taxi choice")

        elif user_input == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                assert isinstance(current_taxi, Taxi)
                try:
                    driving_distance = int(input("Drive how far? "))
                    current_taxi.drive(driving_distance)
                    fare = current_taxi.get_fare()
                    current_bill += fare
                    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                    current_taxi.start_fare()
                except ValueError:
                    print("Driving distance must be a number")
        else:
            print("Invalid option")

        print(f"Bill to date: ${current_bill:.2f}")
        print(MENU)

    print(f"Total trip cost: ${current_bill:.2f}")
    display_taxis(TAXIS)


if __name__ == "__main__":
    main()
