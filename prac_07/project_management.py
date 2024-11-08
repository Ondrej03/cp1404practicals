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

    in_file = open(INPUT_FILE, "r")
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('	')
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        projects.append(project)
    print(f"Loaded {len(projects)} projects from {INPUT_FILE}")







    print(FAREWELL)


main()