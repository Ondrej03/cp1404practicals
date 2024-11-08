"""
CP1404/CP5632 Practical - Guitar exercise
Estimated time : 30 min
Actual time : 7:24
"""

import datetime
from operator import attrgetter


class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __lt__(self, other):
        """primary compared completion status (incomplete come before complete), then compared by priority"""
        if self.is_complete() != other.is_complete():
            return not self.is_complete()
        return self.priority < other.priority

    def __str__(self):
        return (f"{self.name}, start: {self.start_date}, priority: {self.priority}, estimate: ${self.cost_estimate}, "
                f"completion: {self.completion_percentage}%")

    def is_complete(self):
        return self.completion_percentage == "100"


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
                save_to_file(input("Type name of the file to save: "), projects)

            case "D":
                display_projects(projects)

            case "F":
                filter_by_date(projects)

            case "A":
                pass
            case "U":
                pass
            case "Q":
                pass
            case _:
                print("Invalid option")

    print(FAREWELL)


def filter_by_date(projects):
    filter_date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yy): "),
                                             "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    filtered_projects.sort(key=attrgetter('start_date'))
    for project in filtered_projects:
        print(project)


def display_projects(projects):
    projects.sort()
    index = 0
    print("Incomplete projects:")
    while not projects[index].is_complete():
        print(f"    {projects[index]}")
        index += 1
    print("Complete projects:")
    while index < len(projects):
        print(f"    {projects[index]}")
        index += 1


def save_to_file(filename, projects):
    print("Your file is saving")
    out_file = open(filename, "w")
    for project in projects:
        out_file.write(
            f"{project.name}	{project.start_date}	{project.priority}	{project.cost_estimate}"
            f"	{project.completion_percentage}\n")
    out_file.close()
    print("Saved successfully")


def load_projects_from_file(projects, file_name, has_header):
    in_file = open(file_name, "r")

    if has_header:
        # 'Consume' the first line (header) - we don't need its contents
        in_file.readline()

    num_of_lines = 0
    for line in in_file:
        parts = line.strip().split('	')
        project = Project(parts[0], datetime.datetime.strptime(parts[1], "%d/%m/%Y").date(), parts[2],
                          parts[3], parts[4])
        projects.append(project)
        num_of_lines += 1

    print(f"Loaded {num_of_lines} projects from {file_name}")


main()
