"""
CP1404/CP5632 Practical - Project Management Program
Estimated time: 60 min
Actual time: 90 min
"""

import datetime
from operator import attrgetter

from project import Project

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
    """Main function to run the project management program with options to load, save, display, and manage projects."""
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
                add_new_project(projects)
            case "U":
                update_project(projects)
            case _:
                print("Invalid option")

        print(MENU)

    if input("Would you like to save to projects.txt? (Y/n) ").upper() == "Y":
        save_to_file(INPUT_FILE, projects)

    print(FAREWELL)


def update_project(projects):
    """Update the completion percentage and priority of a chosen project from the list of projects."""
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    edited_project = projects[int(input("Project choice: "))]
    print(edited_project)
    new_percentage = input("New percentage: ")
    edited_project.completion_percentage = new_percentage if new_percentage != "" else edited_project.completion_percentage
    new_priority = input("New priority: ")
    edited_project.priority = new_priority if new_priority != "" else edited_project.priority


def add_new_project(projects):
    """Prompt the user to add a new project with its details, then append it to the projects list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    complete = input("Percent complete: ")
    new_project = Project(name, datetime.datetime.strptime(start_date, "%d/%m/%Y").date(),
                          priority, cost, complete)
    projects.append(new_project)
    print(f"New project successfully added: {new_project}")


def filter_by_date(projects):
    """Filter projects by a start date specified by the user and display the filtered list."""
    filter_date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yy): "), "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    filtered_projects.sort(key=attrgetter('start_date'))
    for project in filtered_projects:
        print(project)


def display_projects(projects):
    """Display projects sorted by their completion status and priority."""
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
    """Save the list of projects to a specified file."""
    print("Your file is saving")
    with open(filename, "w") as out_file:
        for project in projects:
            out_file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}"
                f"\t{project.completion_percentage}\n")
    print("Saved successfully")


def load_projects_from_file(projects, file_name, has_header):
    """Load projects from a file, optionally skipping the header, and append them to the projects list."""
    with open(file_name, "r") as in_file:
        if has_header:
            in_file.readline()  # Skip the header line

        num_of_lines = 0
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], datetime.datetime.strptime(parts[1], "%d/%m/%Y").date(), parts[2],
                              parts[3], parts[4])
            projects.append(project)
            num_of_lines += 1

    print(f"Loaded {num_of_lines} projects from {file_name}")


main()
