from A2 import write_to_file, create_file, remove_file, show_file, update_content, search_string, replace_word, show_files

while True:
    try:
        user_selection = input('''
        1. Create File
        2. Remove File
        3. Show File
        4. Update Content 
        5. Search String
        6. Replace Word
        7. Show Files
        0. Exit Program
        \n
        ''')
        
        if user_selection=='0':
            print('Exiting Program')
            break
        elif user_selection == '1':
            create_file()
        elif user_selection == '2':
            remove_file()
        elif user_selection == '3':
            show_file()
        elif user_selection == '4':
            update_content()
        elif user_selection == '5':
            search_string()
        elif user_selection == '6':
            replace_word()
        elif user_selection == '7':
            show_files()
        else:
            print("No command with that code, please select from the aforementioned options\n")
        
    except Exception as  e:
        print(e)
        pass