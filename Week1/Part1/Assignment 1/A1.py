def ask_name_and_priority():
    task_name = input("What task do you wish to insert, Task name: ")
    while True:
        task_priority = input("What is the priority of task you wish to insert\n 1. High\n 2.Medium\n 3.Low\n")
        if task_priority == "1":
            task_priority = "High"
            break
        elif task_priority == "2":
            task_priority = "Medium"
            break
        elif task_priority == "3":
            task_priority = "Low"
            break
        else:
            print("Invalid input")
    return task_name, task_priority

def create_task(Tasks):
    '''
    Create task can add a new task
    '''
    task_name, task_priority = ask_name_and_priority()
    Tasks.append({"Task Name":task_name, "Task Priority":task_priority})   
    list_tasks(Tasks)
    return Tasks


def update_task(Tasks):
    '''
    update task can select an existing task from the list and update it
    '''
    if len(Tasks) == 0:
        print("No tasks assigned, nothing to update")
    else:    
        list_tasks(Tasks)

        while True:
            try:
                task_no = int(input("Where do you wish to insert the task, Task number: "))
                if task_no >= len(Tasks):
                    print("Theres no task present at",task_no,"here are the available tasks")
                    list_tasks(Tasks)
                else:
                    task_name, task_priority = ask_name_and_priority()
                    Tasks[task_no] = {"Task Name":task_name, "Task Priority":task_priority}
                    break   
            except ValueError:
                print("Please enter a valid number for the task")
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
        for i in enumerate(Tasks):
            task_number = i[0]
            print("Task number = ",task_number)
            for j in i[1]:
                print(j,' = ',i[1][j])
            print("\n========================\n")
    return Tasks
