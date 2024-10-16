"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

longest_shortcut = max(len(shortcut) for shortcut in list(CODE_TO_NAME.keys()))
longest_state = max(len(name) for name in list(CODE_TO_NAME.values()))
for shortcut, state in CODE_TO_NAME.items():
    print(f"{shortcut:{longest_shortcut}} is {state:{longest_state}}")

print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")
