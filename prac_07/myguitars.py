"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
"""

from guitar import Guitar


def main():
    """Get guitars from user, sort them, save them into file"""
    guitars = []

    # in_file = open('guitars.csv', 'r')
    # for line in in_file:
    #     parts = line.strip().split(',')
    #     guitar = Guitar(parts[0], parts[1], parts[2])
    #     guitars.append(guitar)
    #
    # in_file.close()

    get_guitars_from_user(guitars)

    guitars.sort()

    save_guitars_to_file(guitars)


def save_guitars_to_file(guitars):
    """Writes saved guitars int guitars.csv file"""
    out_file = open("guitars.csv", "w")
    for guitar in guitars:
        print(guitar)
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()


def get_guitars_from_user(guitars):
    """Gets guitars from user until he input blank name"""
    while (name := input("Name: ")) != "":

        while not (year := input("Year: ")).isdigit():
            print("Enter a valid number")

        while not (cost := input("Cost: ")).isdigit():
            print("Enter a valid number")

        new_guitar = Guitar(name, int(year), int(cost))
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")


main()
