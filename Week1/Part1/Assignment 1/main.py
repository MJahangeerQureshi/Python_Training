from A1 import create_task, update_task, delete_task, list_tasks

Tasks={}

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
            Tasks = create_task(Tasks)
        elif user_selection == 2:
            Tasks = list_tasks(Tasks)
        elif user_selection == 3:
            Tasks = update_task(Tasks)
        elif user_selection == 4:
            Tasks = delete_task(Tasks)
    
    except Exception as  e:
        print(e)
        pass