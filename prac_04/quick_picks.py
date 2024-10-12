import random

NUM_OF_COLUMNS = 6
MIN_NUM = 1
MAX_NUM = 45

def main():

    num_of_picks = int(input("How many quick picks? "))

    for _ in range(num_of_picks):
        row = []
        while len(row) != NUM_OF_COLUMNS:
            random_num = random.randrange(MIN_NUM, MAX_NUM + 1)
            if random_num not in row:
                row.append(random_num)
        row.sort()
        print(" ".join(f"{num:2}" for num in row))

main()