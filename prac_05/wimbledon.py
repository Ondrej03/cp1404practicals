def main():
    champions = []
    countries = set()
    read_data(champions, countries)

    champion_win_count = {}
    for champion in champions:
        if champion in champion_win_count:
            champion_win_count[champion] += 1
        else :
            champion_win_count[champion] = 1

    print_data(champion_win_count, countries)

def read_data(champions, countries):

    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for row in in_file:
            row_elements = row.split(",")
            champions.append(row_elements[2])
            countries.add(row_elements[1])

def print_data(champion_win_count, countries):
    print("Wimbledon Champions: ")
    for champion, win_count in champion_win_count.items():
        print(f"{champion} {win_count}")

    print()
    print("These 12 countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

main()