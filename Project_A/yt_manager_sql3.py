import sqlite3

conn = sqlite3.connect('youtube_videos_db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_all_videos():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print (row)

def add_video(name,time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?,?)",(name,time))
    conn.commit()

def update_video(video_id, name, time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(name,time,video_id))
    conn.commit()

def delete_videos(video_id):
    cur.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()

def main():
    
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List all youtube video ")
        print("2. Add a Youtube video ")
        print("3. Update a Youtube video details")
        print("4. Delete a Youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos()
        
        elif choice == '2':
            name = input("Enter youtube video name: ")
            time = input("Enter video duration: ")
            add_video(name,time)

        elif choice == '3':
            video_id = input("Enter video ID: ")
            name = input("Enter video name to be updated: ")
            time = input("Enter video duration to be updated: ")
            update_video(video_id,name,time)

        elif choice == '4':
            video_id = input("Enter video ID to be deleted: ")
            delete_videos(video_id)

        elif choice == '5':
            break

        else:
            print("Invalid choice!!")


if __name__ == '__main__':
    main()