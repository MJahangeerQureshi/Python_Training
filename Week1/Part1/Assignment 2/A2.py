import os

def write_to_file(fname, mode, data):
    '''
    Write a text file with variable modes
    '''
    if '.' in fname:
        f = open("data/"+fname, mode)
        
    else:
        f = open("data/"+fname+".txt", mode)
    
    f.write(data)
    f.close()

def create_file():
    '''
    Create a text file
    '''
    fname = input("please enter the filename to create : ")
    files=[]
    for i in os.listdir("data"):
        files.append(i.split('.')[0])

    if '.' in fname:
        open("data/"+fname, 'a').close()
        print("File created \n")
    elif fname in files:
        print("file already present, choose to update content insead")
    else:
        open("data/"+fname+'.txt', 'a').close()
        print("File created \n")
    
def remove_file():
    '''
    Delete a text file
    ''' 
    while True:
        fname = input("please enter the filename with its extension to delete : ")
        if fname not in os.listdir("data"):
            print("No file with name present, these are the files available for deletion")
            print(os.listdir("data"))
        else:
            os.remove("data/"+fname)
            break
    print("File removed \n")
    
def show_file():
    '''
    Show the text file
    '''
    while True:
        fname = input("please enter the filename with its extention to show : ")
        if fname not in os.listdir("data"):
            print("No file with name present, these are the files available for visualization")
            print(os.listdir("data"))
        else:
            f = open("data/"+fname,mode='r')
            break
    data = (f.read())
    if data == '':
        print("[SYSTEM MESSAGE : FILE IS EMPTY]")
    else:
        print("[FILE DATA]\n")
        print(data)
    f.close()
    
def update_content():
    '''
    Append or Overwrite the text file
    '''
    
    while True:
        user_preference = input("Do you wish to append or overwrite \n to Overwrite type w\n to Append type a\n")
        if user_preference != "w" and user_preference != "a":
            print("Invalid input, please choose either 'a' or 'w'\n")
        else:
            while True:
                fname = input("please enter the filename with its extention to update : ")
                if fname not in os.listdir("data"):
                    print("No file with name present, these are the files available for update")
                    print(os.listdir("data"))
                else:
                    break
            
            entered_data = input("Please enter your data: ")
            write_to_file(fname, user_preference, entered_data)
            print("File updated \n")
            break
    
def search_string():
    '''
    Search for a phrase in text
    '''
    while True:
        fname = input("please enter the filename with its extention to search in : ")
        if '.' in fname:
            f = open("data/"+fname,mode='r')
            break
        elif fname not in os.listdir("data"):
            print("No file with name present, these are the files available for search")
            print(os.listdir("data"))
        else:
            f = open("data/"+fname+".txt",mode='r')
            break
    string_data = f.read()
    f.close()
    
    if string_data == '':
        print("[SYSTEM MESSAGE : FILE IS EMPTY]")
    else:
        print("[FILE DATA]\n")
        print(string_data)

        search_element = input("please enter the string to search : ")
        lower_index = string_data.find(search_element)
        upper_index = lower_index + len(search_element)
        if lower_index == -1:
            print("Given string isnt present in the File")
        else:
            print("String found at the following lower and upper bounds.")
            print(lower_index, upper_index, "\n")
    
def replace_word():
    '''
    Replace a phrase in a string
    '''
    
    while True:
        fname = input("please enter the filename with its extention to replace in : ")
        if fname not in os.listdir("data"):
            print("No file with name present, these are the files available for replacement")
            print(os.listdir("data"))
        else:
            break
    f = open("data/"+fname,mode='r')
    string_data = f.read()
    f.close()
    
    if string_data == '':
        print("[SYSTEM MESSAGE : FILE IS EMPTY]")
    else:
        print("[FILE DATA]\n")
        print(string_data)
        while True:
            original_string = input("please enter the string you wish to replace : ")
            if string_data.find(original_string) == -1:
                print("Sorry cant find no such word in the file, try again")
            else:
                replacement_string = input("please enter the string you wish to replace it with : ")  
                string_data = string_data.replace(original_string, replacement_string)
                write_to_file(fname,"w", string_data)
                print("String replaced \n")
                break

def show_files():
    print(os.listdir("data"))