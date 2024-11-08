"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
"""

from guitar import Guitar


def main():
    """Read file of programming language details, save as objects, display."""
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], parts[2])
        guitars.append(guitar)

    in_file.close()

    guitars.sort()

    for guitar in guitars:
        print(guitar)


main()


