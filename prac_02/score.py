"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

from random import randrange

def main():
    user_score = float(input("Enter score: "))
    print(get_score(user_score))

    print(get_score(randrange(0,105)))


def get_score(user_score):
    if user_score < 0:
        return "Invalid score"
    elif user_score > 100:
        return "Invalid score"
    elif user_score > 90:
        return "Excellent"
    elif user_score > 50:
        return "Passable"
    elif user_score < 50:
        return "Bad"

main()