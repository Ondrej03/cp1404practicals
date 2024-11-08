"""
CP1404/CP5632 Practical - Programming languages exercise
Estimated time : 20 mins
Actual time spent : 25 min
"""

from guitar import Guitar

def main():
    print("My guitars!")
    my_guitars = []

    while (name := input("Name: ")) != "":

        while not (year := input("Year: ")).isdigit():
            print("Enter a valid number")

        while not (cost := input("Cost: ")).isdigit():
            print("Enter a valid number")

        new_guitar = Guitar(name, int(year), int(cost))
        my_guitars.append(new_guitar)
        print(f"{new_guitar} added.")


    print("These are my guitars: ")
    for index, guitar in enumerate(my_guitars):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {index + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")








main()