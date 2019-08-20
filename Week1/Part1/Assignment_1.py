def Create_Task():
    'Create task can add a task at the end of the list or between any two tasks.'
    if len(Tasks)==0:
        task_name = input("What task do you wish to insert, Task name: ")
        Tasks.append(task_name)
    else:
        List_Tasks()

        task_no = int(input("Where do you wish to insert the task, Task number: "))
        task_name = input("What task do you wish to insert, Task name: ")
        Tasks.insert(task_no, task_name)
    
def Update_Task():
    'For update a task select a task from the list and update it.'
    if len(Tasks) == 0:
        print("No tasks assigned, nothing to delete")
    else:    
        List_Tasks()
        task_no = input("Which task do you wish to update, Task number: ")
        task_name = input("Whats the Task name, Task name: ")
        Tasks[task_no] = task_name

def Delete_Task(): 
    'Delete a specific task.'
    if len(Tasks) == 0:
        print("No tasks assigned, nothing to delete")
    else:
        List_Tasks()

        task_no = int(input("Which task do you wish to delete, Task number: "))

        Tasks.pop(task_no)

def List_Tasks():
    'List Tasks should display a list of all the tasks that were added by the user.'
    t_no=0
    if len(Tasks) == 0:
        print("No entries in To-Do list")
    else:
        for i in Tasks:
            print(t_no, i)
            t_no += 1


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
        elif user_selection==1:
            Create_Task()
        elif user_selection==2:
            List_Tasks()
        elif user_selection==3:
            Update_Task
        elif user_selection==4:
            Delete_Task()
    except Exception as  e:
        print(e)
        pass