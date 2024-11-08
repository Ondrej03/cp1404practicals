"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
"""
from os import write

from guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []


    # in_file = open('guitars.csv', 'r')
    # for line in in_file:
    #     parts = line.strip().split(',')
    #     guitar = Guitar(parts[0], parts[1], parts[2])
    #     guitars.append(guitar)
    #
    # in_file.close()

    while (name := input("Name: ")) != "":

        while not (year := input("Year: ")).isdigit():
            print("Enter a valid number")

        while not (cost := input("Cost: ")).isdigit():
            print("Enter a valid number")

        new_guitar = Guitar(name, int(year), int(cost))
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")

    guitars.sort()

    out_file = open("guitars.csv", "w")
    for guitar in guitars:
        print(guitar)
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()


main()


