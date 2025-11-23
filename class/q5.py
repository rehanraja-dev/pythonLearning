class Playlist: 
    def __init__(self,name):
        self.name = name
        self.songs = []
    
    def add_song(self,song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self,song):
        self.songs.remove(song)
        print(f"removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}': ")
        for song in self.songs:
            print(song)

get_playlist = Playlist("Favorite Sonngs")
get_playlist.add_song("Ishq")
get_playlist.add_song("Hawa banke")
get_playlist.show_songs()
get_playlist.remove_song(0)
get_playlist.show_songs()