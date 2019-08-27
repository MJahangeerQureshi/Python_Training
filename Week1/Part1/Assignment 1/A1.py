def create_task(Tasks):
    '''
    Create task can add a task at the end of the list or between any two tasks
    '''
    if len(Tasks) == 0:
        task_name = input("What task do you wish to insert, Task name: ")
        Tasks.update({"0":task_name})
    else:
        list_tasks(Tasks)
        
        while True:
            try:
                task_no = input("Where do you wish to insert the task, Task number: ")
                if task_no in list(Tasks):
                    print("Theres already a task present at",task_no," try at a different number")
                else:
                    task_name = input("What task do you wish to insert, Task name: ")
                    Tasks.update({task_no:task_name})
                    break
            except ValueError:
                print("Please enter a valid number for the task")
    return Tasks


def update_task(Tasks):
    '''
    For update a task select a task from the list and update it
    '''
    if len(Tasks) == 0:
        print("No tasks assigned, nothing to update")
    else:    
        list_tasks(Tasks)
        
        while True:
            task_no = input("Which task do you wish to update, Task number: ")
            if task_no not in list(Tasks):
                print("Sorry no task present with that Task number, here are the available tasks. try again")
                list_tasks(Tasks)
            else:
                task_name = input("Whats the Task name, Task name: ")
                Tasks.update({task_no:task_name})
                break
    return Tasks


def delete_task(Tasks): 
    '''
    Delete a specific task.
    '''
    if len(Tasks) == 0:
        print("No tasks assigned, nothing to delete")
    else:
        list_tasks(Tasks)
        
        task_no = input("Which task do you wish to delete, Task number: ")
        del Tasks[task_no]

    return Tasks


def list_tasks(Tasks):
    '''
    List Tasks should display a list of all the tasks that were added by the user
    '''
    if len(Tasks) == 0:
        print("No entries in To-Do list")
    else:
        for t in Tasks:
            print(t, Tasks[t])
    return Tasks
