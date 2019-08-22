import os

def CreateFile():
    'Create a text file'
    
    fname = input("please enter the filename to create : ")
    os.mknod(fname+".txt")
    print("File created \n")
    
def RemoveFile():
    'Delete a text file'
    
    fname = input("please enter the filename to delete : ")
    os.remove(fname+".txt")
    print("File removed \n")
    
def ShowFile():
    'Show the text file'
    
    fname = input("please enter the filename to show : ")
    f = open(fname+".txt",mode='r')
    print(f.read())
    f.close()
    
def UpdateContent():
    'Append or Overwrite the text file'
    
    while True:
        user_preference = input("Do you wish to append or overwrite \n 1 Overwrite \n 2 Append \n")
        if user_preference == "1":
            fname = input("please enter the filename to update : ")
            entered_data = input("Please enter your data: ")
            f = open(fname+".txt", "w")
            f.write(entered_data)
            f.close()
            print("File updated \n")
            break
        elif user_preference == "2":
            fname = input("please enter the filename to update : ")
            entered_data = input("Please enter your data: ")
            f = open(fname+".txt", "a")
            f.write(entered_data)
            f.close()
            print("File updated \n")
            break
        elif user_preference == "0":
            break
        else:
            print("Invalid input, please choose either 1 or 2, if you wish to enter 0 \n")
    
def SearchString():
    'Search for a phrase in text'
    
    fname = input("please enter the filename to show : ")
    f = open(fname+".txt",mode='r')
    string_data = f.read()
    f.close()
    
    search_element = input("please enter the string to search : ")
    lower_index = string_data.find(search_element)
    upper_index = lower_index + len(search_element)
    if lower_index < 0:
        print("Given string isnt present in the File")
    else:
        print("String found at the following lower and upper bounds.")
        print(lower_index, upper_index, "\n")
    
    
    string_data[lower_index:upper_index]
    
def ReplaceWord():
    'Replace a phrase in a string'
    
    fname = input("please enter the filename to show : ")
    f = open(fname+".txt",mode='r')
    string_data = f.read()
    f.close()
    
    original_string = input("please enter the string you wish to replace : ")
    replacement_string = input("please enter the string you wish to replace it with : ")
    
    string_data = string_data.replace(original_string, replacement_string)
    
    f = open(fname+".txt", "w")
    f.write(string_data)
    f.close()
    print("String replaced \n")


Tasks=[]
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