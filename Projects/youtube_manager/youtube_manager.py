import json

fileName = "database.json"

def saveDataHelper(videos):
    with open(fileName, 'w') as file:
        json.dump(videos, file)


def loadAllVideos():
    try:
        with open(fileName, 'r') as file:
           return json.load(file)
    except FileNotFoundError:
        return []

def showAllVideos(videos):
    print("*" * 50)

    for index, video in enumerate(videos, start=1):
        print(f"{index}, {video['name']} - {video['time']}")

    print("*" * 50)

def addVideo(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration: ")
    videos.append({'name': name, 'time':time})
    saveDataHelper(videos)

def updateVideo(videos):
    showAllVideos(videos)
    index = int(input('Enter the number you want to update: '))
    if 1<= index <= len(videos):
        name = input("Enter video name: ")
        time = input("Enter video duration: ")
        videos[index-1] = {"name": name, "time": time}
        saveDataHelper(videos)
    else: 
        print('\n Enter the valid number')

def deleteVideo(videos):
    showAllVideos(videos)
    index = int(input('Enter the number you want to delete: '))
    if 1<= index <= len(videos):
        del videos[index-1]
        saveDataHelper(videos)
    else:
        print("Enter the valid number")

def main():
    while True:
        videos = loadAllVideos()
        print("\n Youtube Manager")
        print("""
        1. List all files 
        2. Add youtube video
        3. Update youtube video details
        4. Delete youtube video
        5. Exit the app
        """)
        choice = input("Select the option: ")
        match choice:
            case "1":
                showAllVideos(videos)
            case "2":
                addVideo(videos)
            case "3":
                updateVideo(videos)
            case "4":
                deleteVideo(videos)
            case "5":
                break
            case _:
                print("Invalid selected option")

if __name__ == "__main__" :
    main()