from traceback import print_tb

MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit
"""

def main():
    print(MENU)
    score = -1
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_score(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Finished.")

def get_valid_score():
    user_score = int(input("Type your score :"))
    while user_score < 0 or user_score > 100:
        print("Invalid score")
        user_score = int(input("Type your score"))
    return user_score

def print_score(score):
    if score == -1:
        print("No score recorded")
    else:
        if score > 90:
            print("Excellent")
        elif score > 50:
            print("Passable")
        elif score < 50:
            print("Bad")
        else:
            print("Invalid score")

def show_stars(score):
    if score == -1:
        print("No score recorded")
    else:
        print("*" * score)

main()

