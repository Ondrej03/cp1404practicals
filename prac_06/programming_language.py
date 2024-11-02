"""
CP1404/CP5632 Practical - Programming language class
"""

class ProgrammingLanguage:
    def __init__(self, name, language_type, is_reflective, release_year):
        self.name = name
        self.language_type = language_type
        self.is_reflective = is_reflective
        self.release_year = release_year

    def __str__(self):
        return (f"{self.name}, {self.language_type} Typing, Reflection={self.is_reflective}, "
                f"First appeared in {self.release_year}")

    def is_dynamic(self):
        return True if self.language_type.toupper == "DYNAMIC" else False

