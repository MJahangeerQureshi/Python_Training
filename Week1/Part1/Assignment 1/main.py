from A1 import CreateTask, UpdateTask, DeleteTask, ListTasks

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