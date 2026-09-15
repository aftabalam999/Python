from pathlib import Path

def createFile():
    try:
        name = input('\n please tell your file name with extention :- ')
        path = Path(name)

        if not path.exists() :
            with open(path, 'w') as fs:
                data = input('What you want to write :- ')
                fs.write(data)
            print('your file is created successfully ')
        else:
            print('Error file name already exists')
    except Exception as err:
        print(f"an error occured as {err}")

def readFile():
    try:
        name = input('\n please tell your file name with extention :- ')
        path = Path(name)

        if path.exists():
            with open(path, 'r') as fs:
                content = fs.read()
                print(f"your file content is : \n {content}")
        else :
            print('Error file name not exists')
    except Exception as err:
        print(f"an error occured as {err}")

def updateFile():
    try:
        name = input('\n please tell your file name with extention :- ')
        path = Path(name)
        if path.exists():
            print(""" Operations
                1. Renaming the file
                2. Appending the content
                3. Overwriting the file
                """)
            choice = int(input("Enter your option :- "))

            if choice == 1:
                newName = input('\n please tell your new file name with extention :- ')
                newPath = Path(newName)
                if not newPath.exists():
                    path.rename(newPath)
                    print("File renamed successfully")
                else:
                    print("File name is already exists")
            if choice == 2 :
                with open(path, 'a') as fs:
                    content = input("\n Write here what you want to append :- ")
                    fs.write(f"\n {content}")
                    print("Your content append successfully")
            if choice == 3:
                with open(path, 'w') as fs:
                    data = input('Write the text that you want to overwrite :- ')
                    fs.write(data)
                    print("Your content overwritten successfully")
        else :
            print('Error file name not exists')
    except Exception as err:
        print(f"an error occured as {err}")

def deleteFile():
    try:
        name = input('\n please tell your file name with extention :- ')
        path = Path(name)

        if path.exists():
            path.unlink()
            print('File is deleted Successfully')
        else:
            print('Error : File does not exists')
    except Exception as err:
        print(f"Error: Some error occure {err}")

print("""
press 1 for create the file
press 2 for reading the file
press 3 for updating the file
press 4 for deleting the file
""")

user_input = int(input('\n tell your response :- '))
if user_input == 1 :
    createFile()
if user_input == 2 :
    readFile()
if user_input == 3 :
    updateFile()
if user_input == 4 :
    deleteFile()