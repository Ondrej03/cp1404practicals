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






    print(champions)
    print(countries)


def read_data(champions, countries):

    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        for row in in_file:
            row_elements = row.split(",")
            champions.append(row_elements[2])
            countries.add(row_elements[1])


main()