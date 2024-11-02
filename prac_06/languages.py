"""
CP1404/CP5632 Practical - Programming languages exercise
Estimated time : 20 mins
Actual time spent : 12 mins
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]

print("The dynamically typed languages are:")
for language in programming_languages:
    if language.is_reflective:
        print(language.name)