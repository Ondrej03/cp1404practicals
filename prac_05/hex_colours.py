"""
CP1404/CP5632 Practical
"""

COLOURS = {"CELADON": "#ace1af", "CERULEAN": "#007ba7", "CHAMPAGNE": "#f7e7ce",
          "CARMINE": "#960018", "CARDINAL": "#c41e3a", "CANARY": "#ffff99",
          "CAMEL": "#c19a6b", "BYZANTINE": "#bd33a4","BONE": "#e3dac9",
          "BEIGE": "#f5f5dc"}

color = input("Enter color name: ").upper()
while color != "":
    try:
        print(color, "code is", COLOURS[color])
    except KeyError:
        print("Invalid color name")
    color = input("Enter color name: ").upper()