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



    print(FAREWELL)


main()