from A2 import WriteToFile, CreateFile, RemoveFile, ShowFile, UpdateContent, SearchString, ReplaceWord

while True:
    try:
        user_selection = int(input('''
        1. Create File
        2. Remove File
        3. Show File
        4. Update Content 
        5. Search String
        6. Replace Word
        0. Exit Program
        \n
        '''))
        
        if user_selection==0:
            print('Exiting Program')
            break
        elif user_selection == 1:
            CreateFile()
        elif user_selection == 2:
            RemoveFile()
        elif user_selection == 3:
            ShowFile()
        elif user_selection == 4:
            UpdateContent()
        elif user_selection == 5:
            SearchString()
        elif user_selection == 6:
            ReplaceWord()
        
    except Exception as  e:
        print(e)
        pass