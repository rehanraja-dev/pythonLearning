import json


data_file = "youtube.txt"
def load_data():
    try:
        with open(data_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(data_file, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter Youtube video name: ")
    time = input("Enter video duration: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    index = int(input("Enter video number to update: "))
    if index >= 1 and index <= len(videos):
        name = input("Enter the video name: ")
        time = input("Enter the video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
        print("Video is succesfully updated!!")
    else:
        print("Invalid index selected")

def delete_videos(videos):
    index = int(input("Enter video number to be deleted: "))
    if index >= 1 and index <=len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Video is deleted succesfully!!")
    else:
        print("Invalid video number selected")

def main():

    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List all youtube video ")
        print("2. Add a Youtube video ")
        print("3. Update a Youtube video details")
        print("4. Delete a Youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)

            case '2':
                add_video(videos)
            
            case '3':
                update_video(videos) 

            case '4':
                delete_videos(videos)
            
            case '5':
                break

            case _:
                print("Invalid Choice!!")

if __name__ == "__main__":
    main()



