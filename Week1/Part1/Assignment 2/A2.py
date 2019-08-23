import os

def WriteToFile(fname, mode, data):
    '''
    Write a text file with variable modes
    '''
    f = open(fname+".txt", mode)
    f.write(data)
    f.close()

def CreateFile():
    '''
    Create a text file
    '''
    fname = input("please enter the filename to create : ")
    open(fname+'.txt', 'a').close()
    print("File created \n")
    
def RemoveFile():
    '''
    Delete a text file
    ''' 
    fname = input("please enter the filename to delete : ")
    os.remove(fname+".txt")
    print("File removed \n")
    
def ShowFile():
    '''
    Show the text file
    '''
    
    fname = input("please enter the filename to show : ")
    f = open(fname+".txt",mode='r')
    print(f.read())
    f.close()
    
def UpdateContent():
    '''
    Append or Overwrite the text file
    '''
        
    while True:
        user_preference = input("Do you wish to append or overwrite \n to Overwrite type w\n to Append type a\n")
        if user_preference != "w" and user_preference != "a":
            print("Invalid input, please choose either 'a' or 'w'\n")
        else:
            fname = input("please enter the filename to update : ")
            entered_data = input("Please enter your data: ")
            WriteToFile(fname, user_preference, entered_data)
            print("File updated \n")
            break
    
def SearchString():
    '''
    Search for a phrase in text
    '''
    fname = input("please enter the filename to show : ")
    f = open(fname+".txt",mode='r')
    string_data = f.read()
    f.close()
    
    search_element = input("please enter the string to search : ")
    lower_index = string_data.find(search_element)
    upper_index = lower_index + len(search_element)
    if lower_index == -1:
        print("Given string isnt present in the File")
    else:
        print("String found at the following lower and upper bounds.")
        print(lower_index, upper_index, "\n")
    
def ReplaceWord():
    '''
    Replace a phrase in a string
    '''
    
    fname = input("please enter the filename to show : ")
    f = open(fname+".txt",mode='r')
    string_data = f.read()
    f.close()
    
    original_string = input("please enter the string you wish to replace : ")
    if string_data.find(original_string) == -1:
        print("Sorry cant find that word")
    else:
        replacement_string = input("please enter the string you wish to replace it with : ")  
        string_data = string_data.replace(original_string, replacement_string)
        WriteToFile(fname,"w", string_data)
        print("String replaced \n")
