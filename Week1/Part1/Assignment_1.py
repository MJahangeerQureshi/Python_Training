def CreateTask(Tasks):
    'Create task can add a task at the end of the list or between any two tasks.'
    if len(Tasks)==0:
        task_name = input("What task do you wish to insert, Task name: ")
        Tasks.append(task_name)
    else:
        ListTasks(Tasks)

        task_no = int(input("Where do you wish to pytinsert the task, Task number: "))
        task_name = input("What task do you wish to insert, Task name: ")
        Tasks.insert(task_no, task_name)
    return Tasks
    
def UpdateTask(Tasks):
    'For update a task select a task from the list and update it.'
    if len(Tasks) == 0:
        print("No tasks assigned, nothing to delete")
    else:    
        ListTasks(Tasks)
        
        task_no = input("Which task do you wish to update, Task number: ")
        task_name = input("Whats the Task name, Task name: ")
        Tasks[task_no] = task_name
    return Tasks

def DeleteTask(Tasks): 
    'Delete a specific task.'
    if len(Tasks) == 0:
        print("No tasks assigned, nothing to delete")
    else:
        ListTasks(Tasks)

        task_no = int(input("Which task do you wish to delete, Task number: "))
        Tasks.pop(task_no)
    return Tasks

def ListTasks(Tasks):
    'List Tasks should display a list of all the tasks that were added by the user.'
    task_no=0
    if len(Tasks) == 0:
        print("No entries in To-Do list")
    else:
        for t in Tasks:
            print(task_no, t)
            task_no += 1
    return Tasks

Tasks=[]

while True:
    try:
        user_selection = int(input('''
        1. Create a Task
        2. List tasks
        3. Update a Task
        4. Delete a Task 
        0. Exit Program
        \n
        '''))
        
        if user_selection==0:
            print('Exiting Program')
            break
        elif user_selection == 1:
            Tasks = CreateTask(Tasks)
        elif user_selection == 2:
            Tasks = ListTasks(Tasks)
        elif user_selection == 3:
            Tasks = UpdateTask(Tasks)
        elif user_selection == 4:
            Tasks = DeleteTask(Tasks)
    
    except Exception as  e:
        print(e)
        pass