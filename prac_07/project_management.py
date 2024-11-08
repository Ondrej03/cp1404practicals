"""
CP1404/CP5632 Practical - Guitar exercise
Estimated time : 30 min
Actual time : 7:24
"""


class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage


INPUT_FILE = "projects.txt"

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

GREETING = "Welcome to Pythonic Project Management"
FAREWELL = "Thank you for using custom-built project management software."


def main():
    print(GREETING)

    projects = []

    load_projects_from_file(projects, INPUT_FILE, True)

    print(MENU)
    while (user_input := input(">>> ")).upper() != "Q":
        match user_input.upper():

            case "L":

                try:
                    load_projects_from_file(projects, input("Input file name: "),
                                            input("Does file include header? (Y/n) ").upper() == "Y")
                except FileNotFoundError:
                    print("File not found, no new project loaded")

            case "S":
                pass
            case "D":
                pass
            case "F":
                pass
            case "A":
                pass
            case "U":
                pass
            case "Q":
                pass
            case _:
                print("Invalid option")

    print(FAREWELL)


def load_projects_from_file(projects, file_name, has_header):
    in_file = open(file_name, "r")

    if has_header:
        # 'Consume' the first line (header) - we don't need its contents
        in_file.readline()

    num_of_lines = 0
    for line in in_file:
        parts = line.strip().split('	')
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        projects.append(project)
        num_of_lines += 1

    print(f"Loaded {num_of_lines} projects from {file_name}")


main()
