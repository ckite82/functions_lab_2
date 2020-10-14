# As a user, to manage my task list I would like a program that allows me to:

# Print a list of uncompleted tasks

# Print a list of completed tasks

# Print a list of all task descriptions

# Print a list of tasks where time_taken is at least a given time

# Print any task with a given description




tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def list_of_tasks(tasks):
    for task in tasks:
        if task ["completed"] == False:
            print(task["description"])
# list_of_tasks(tasks)

def list_of_completed_tasks(tasks):
    for task in tasks:
        if task ["completed"] == True:
            print(task["description"])

# list_of_completed_tasks(tasks)

def list_of_task_descriptions(tasks):
    for task in tasks:
        print(task["description"])

# list_of_task_descriptions(tasks)

def time_taken(tasks, time_taken):
    for task in tasks:
        if task["time_taken"] >= time_taken:
            print(task["description"])
            
# time_taken(tasks, 25)

def given_description(tasks, given_description):
    for task in tasks:
        if task["description"] == given_description:
            print(task)
            
# given_description(tasks, "Make Dinner")

# Given a description update that task to mark it as complete.

def update_task(tasks, description):
    for task in tasks:
        if task["description"] == description:
            task["completed"] = True
            print(task)

# update_task(tasks, "Feed Cat")

# add a task to the list

def add_task(tasks):
    tasks.append({"description": "Wash Clothes", "completed": False, "time_taken": 45 })

add_task(tasks)
print(tasks)