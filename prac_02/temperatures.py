"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_cel_to_fahr(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahr_to_cel(fahrenheit)
            print(f"Result: {celsius:.2f} C")

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahr_to_cel(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_cel_to_fahr(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()