import os

def directory_choice():
    directories = [content for content in os.listdir(os.getcwd()) if os.path.isdir(content)]
    print("Please select a directory:", directories, sep = "\n")
    usr_direct = input("please select a directory: ")
    if os.path.isdir(usr_direct):
        return usr_direct
    else:
        print("That is not a valid directory, try again.")
        return directory_choice()

def print_files(direct):
    path = os.path.join(os.getcwd(), direct)
    os.chdir(path)
    files = [print(content) for content in os.listdir(os.getcwd()) if os.path.isfile(content)]        

# main 
print_files(directory_choice())

