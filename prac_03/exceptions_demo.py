"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - When numerator or denominator would not be a valid int values
2. When will a ZeroDivisionError occur?
    - When denominator would be 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")